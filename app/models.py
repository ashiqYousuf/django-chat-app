from django.db import models
from django.contrib.auth.models import User


# A chat room (Group) can have one or many users
# Also a member can be a part of one of more chat rooms (Groups)
# Implies MANYTOMANY Relation
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

# Actual Chat Message
# It should have a room field (F.K)
# It should have a sender and receiver (F.K's)
# A sender can have many Receivers
# A receiver can receive from many senders
class Chat(models.Model):
    # room.chats.all()
    room = models.ForeignKey(ChatRoom , on_delete=models.CASCADE , related_name='chats')
    # user.sent_chats.all(): to get all chats sent by a particular user
    # user.sent_chats.filter(receiver=user1): to get all chats sent by a particular user to a specific receiver
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sent_chats')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name='received_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return f'{self.sender} - {self.receiver} : {self.room}'
