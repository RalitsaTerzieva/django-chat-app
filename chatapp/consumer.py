from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]['kwargs']['room_name']