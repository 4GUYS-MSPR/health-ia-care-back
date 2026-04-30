from django.urls import re_path

from app.consumers import MemberConsumer

from logs.consumers import LogConsumer

from social_network.consumers import LikeConsumer

websocket_urlpatterns = [
    re_path(r'api/ws/logs/$', LogConsumer.as_asgi()),
    re_path(r'api/ws/likes/$', LikeConsumer.as_asgi()),
    re_path(r'api/ws/new-24h-members/$', MemberConsumer.as_asgi()),
]
