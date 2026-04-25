import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LogConsumer(AsyncWebsocketConsumer):
    async def label(self):
        return "logs_group"

    async def connect(self):
        await self.channel_layer.group_add("logs", self.channel_name)
        await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard("logs", self.channel_name)

    async def log_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
