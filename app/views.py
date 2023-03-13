from django.shortcuts import render
from .models import ChatRoom , Chat , User
from django.http import HttpResponse
# Create your views here.
def home(request , receiver):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>Please Login First</h1>")
    user_pair = [request.user.username , receiver]
    user_pair.sort()
    room_name = f'chat_{user_pair[0]}_{user_pair[1]}'
    # Get ChatRoom Object
    chat_room = ChatRoom.objects.filter(name=room_name).first()
    messages = []
    # if chatroom does'nt exist create one
    if not chat_room:
        chat_room = ChatRoom.objects.create(name=room_name)
        chat_room.members.add(request.user , User.objects.get(username=receiver))
    # retrieve all chat from Chat model where room is: chat_room in such a way so that we could distinguish between the messages of the sender and the receiver
    else:
        chat_messages =  Chat.objects.filter(room=chat_room)
        for message in chat_messages:
            if message.sender == request.user:
                messages.append({"text": message.message ,"timestamp": message.timestamp , "username": request.user.username}) # or message.sender.username
            elif message.receiver == request.user:
                messages.append({"text": message.message , "timestamp": message.timestamp , "username": message.sender.username})
    
    return render(request , 'home.html' ,{'receiver': receiver , 'messages': messages})
