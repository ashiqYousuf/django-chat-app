from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import ChatRoom , Chat
from django.contrib.auth.models import User
from django.utils import timezone

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self , event):
        self.receiver = self.scope['url_route']['kwargs']['receiver']
        self.user = self.scope['user']
        self.room_name = None

        if not self.user.is_authenticated or not User.objects.filter(username=self.receiver).first():
            self.send({
                'type': 'websocket.close',
            })
            raise StopConsumer()
        else:
            user_pair = [self.user.username , self.receiver]
            user_pair.sort()
            self.room_name = f'chat_{user_pair[0]}_{user_pair[1]}'

            async_to_sync(self.channel_layer.group_add)(
                self.room_name,
                self.channel_name,
            )
            self.send({
                'type': 'websocket.accept'
            })
    
    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name,
        )
        raise StopConsumer()
    
    def websocket_receive(self , event):
        data = json.loads(event['text'])
        data['user'] = self.user.username
        data['receiver'] = self.receiver
        room = ChatRoom.objects.get(name=self.room_name)
        receiver = User.objects.get(username=self.receiver)
        chat = Chat(room=room , sender=self.user , receiver=receiver , message=data['msg'])
        chat.save()
        data['timestamp'] = timezone.now().isoformat()
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat.message',
                'message': json.dumps(data)
            }
        )
    
    def chat_message(self , event):
        self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })
