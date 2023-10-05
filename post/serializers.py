from rest_framework import serializers
from .models import Save, Post, Story
from .models import Location, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'description', 'created_date']
        extra_kwargs = {
            "article": {"required": False}
        }

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        return Comment.objects.create(user_id=user_id, **validated_data)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('title',)


class PostGetSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'image', 'location', 'description', 'comment', 'created_date')


class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'location', 'description', 'created_date')

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        return Post.objects.create(user_id=user_id, **validated_data)


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = ('id', 'user', 'post')


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['id', 'content', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        return Story.objects.create(user_id=user_id, **validated_data)

