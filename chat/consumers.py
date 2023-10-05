import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token

from .models import Room, Message


class RoomConsumer(AsyncWebsocketConsumer):
    async def get_user(self, token):
        Account = get_user_model()
        try:
            token_key = token
            token = await database_sync_to_async(Token.objects.get)(key=token_key)
            return await database_sync_to_async(Account.objects.get)(pk=token.user_id)
        except (Token.DoesNotExist, Account.DoesNotExist):
            return None

    async def connect(self):
        self.token = self.scope["query_string"].decode("utf-8").split("=")[1]
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        account = await self.get_user(self.token)

        if not account.is_authenticated:
            await self.close()

        self.scope["account"] = account

        try:
            self.room = await database_sync_to_async(Room.objects.get)(
                id=self.room_name
            )

        except Room.DoesNotExist:
            await self.close()

        if account not in await database_sync_to_async(list)(self.room.account.all()):
            await self.close()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        user = self.scope["user"]
        user_id = user.id
        message = text_data

        message_obj = await database_sync_to_async(Message.objects.create)(
            room=self.room, user_id=user_id, message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "message",
                "message": message_obj.message,
                "user": user.username,
                "created_date": message_obj.created_date.isoformat(),
            },
        )

    async def message(self, event):
        message = event["message"]
        user = event["user"]
        created_date = event["created_date"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "account": user,
                    "created_date": created_date,
                }
            )
        )