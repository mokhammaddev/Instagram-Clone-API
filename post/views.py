from rest_framework import generics, permissions
from .models import Post, Save, Story
from .serializers import PostPostSerializer, PostGetSerializer,  SaveSerializer, StorySerializer
from .models import Location, Comment
from .serializers import LocationSerializer, CommentSerializer


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/post/comment/{post_id}/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostPostSerializer
        return PostGetSerializer


class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPostSerializer


class SaveListCreateAPIView(generics.ListCreateAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveDeleteAPIView(generics.DestroyAPIView):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class StoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer



