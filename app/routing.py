from django.urls import path
from . consumers import MySyncConsumer


websocket_urlpatterns = [
    path('ws/<str:receiver>/' , MySyncConsumer.as_asgi()),
]
