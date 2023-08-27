from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache
import json
from .models import ChatMessage


class ChatConsumer(WebsocketConsumer):
    CACHE_EXPIRY_TIME = 600

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        self.accept()

        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        # Leave the chat room group
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json.get('command', None)

        if command == 'fetch_messages':
            previous_messages = cache.get(f'chat_{self.room_name}')
            if previous_messages:
                self.send_previous_messages(previous_messages)
        elif command == 'send_message':
            message = text_data_json['message']
            self.save_and_send_message(message)
            self.create_chat_message(message)
        elif command == 'send_file':
            file_data = text_data_json['file_data']
            caption = text_data_json['caption']
            self.save_and_send_file(file_data, caption)
            self.create_chat_message(file_data, caption)

    def send_previous_messages(self, previous_messages):
        for message in previous_messages:
            self.send(text_data=json.dumps({
                'message': message
            }))

    def save_and_send_message(self, message):
        self.save_message_to_cache(message)
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    def save_and_send_file(self, file_data, caption):
        file_message = {
            'file_data': file_data,
            'caption': caption,
            'is_file': True
        }
        self.save_message_to_cache(file_message)
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': file_message
            }
        )

    def create_chat_message(self, message, caption=None):
        ChatMessage.objects.create(
            room_name=self.room_name,
            message=message,
            image=caption
        )

    def save_message_to_cache(self, message):
        previous_messages = cache.get(f'chat_{self.room_name}', [])
        previous_messages.append(message)
        cache.set(f'chat_{self.room_name}', previous_messages, self.CACHE_EXPIRY_TIME)
