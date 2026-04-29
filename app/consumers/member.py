import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MemberConsumer(AsyncWebsocketConsumer):
    async def label(self):
        return "members_group"

    async def connect(self):
        await self.channel_layer.group_add("members", self.channel_name)
        await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard("members", self.channel_name)

    async def member_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
