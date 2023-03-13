from app.views import home
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/<str:receiver>/',home,name='home'),
]
