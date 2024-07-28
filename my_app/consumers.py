from channels.generic.websocket import AsyncWebsocketConsumer
from django.apps import apps
from asgiref.sync import sync_to_async
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = f'user_{self.user.id}'
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        recipient_username = text_data_json['recipient']
        User = apps.get_model('auth', 'User')

        # استفاده از sync_to_async برای تبدیل عملیات همزمان به غیرهمزمان
        recipient = await sync_to_async(User.objects.get)(username=recipient_username)
        message = text_data_json['message']

        # Save message to database
        Message = apps.get_model('my_app', 'Message')
        await sync_to_async(Message.objects.create)(sender=self.user, recipient=recipient, content=message)

        # Send message to recipient
        recipient_room_name = f'user_{recipient.id}'
        recipient_group_name = f'chat_{recipient_room_name}'
        await self.channel_layer.group_send(
            recipient_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
