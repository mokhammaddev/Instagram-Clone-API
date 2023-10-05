from rest_framework import serializers
from .models import Message, Room
from django.contrib.auth import get_user_model
from account.serializers import MyProfileSerializer


#
# class RoomSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Room
#         fields = ['id', 'user', 'name']
#
#
# class MessageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Message
#         fields = ['id', 'user', 'room', 'message', 'created_date']


class RoomSerializer(serializers.ModelSerializer):
    user = MyProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['id', 'user']

    def get_user(self, obj):
        user_ids = obj.members.all()
        user = get_user_model().objects.filter(id__in=user_ids)
        return user.values("id", "username")


class RoomMessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"

    def get_user(self, obj):
        user_id = obj.user.id
        user = get_user_model().objects.get(id=user_id)
        return {"id": user.id, "username": user.username}


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'room', 'message']


class RoomWithMessagesSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['id', 'user', 'message']

