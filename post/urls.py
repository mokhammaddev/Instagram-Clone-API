from django.urls import path
from .views import (PostListCreateAPIView, PostRUDAPIView, SaveListCreateAPIView, SaveDeleteAPIView, StoryDeleteAPIView,
                    StoryListCreateAPIView, LocationListCreateAPIView, LocationRUDAPIView, CommentListCreateAPIView)


urlpatterns = [
    # post
    path('post/', PostListCreateAPIView.as_view()),
    path('post/<int:pk>/', PostRUDAPIView.as_view()),
    # save
    path('save/', SaveListCreateAPIView.as_view()),
    path('save/<int:pk>/', SaveDeleteAPIView.as_view()),
    # story
    path('story/', StoryListCreateAPIView.as_view()),
    path('story/<int:pk>/', StoryDeleteAPIView.as_view()),
    # location
    path('location/', LocationListCreateAPIView.as_view()),
    path('location/<int:pk>/', LocationRUDAPIView.as_view()),
    # comment
    path('comment/', CommentListCreateAPIView.as_view()),
]
