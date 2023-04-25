from django.shortcuts import render
from .models import ChatRoom,ChatMessage


def index(request):
    chat_rooms = ChatRoom.objects.all()
   
    return render(request,'chatapp/index.html',{'chat_rooms':chat_rooms})


def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    message = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html',{'chatroom':chatroom,'message':message})