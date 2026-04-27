from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .levels import LogLevel
from .models import Log
from .serializers import LogSerializer

@receiver(post_save, sender=Log)
def announce_log_update(sender, instance, **kwargs): # pylint: disable=unused-argument
    if instance.level not in [LogLevel.WARNING.name, LogLevel.ERROR.name]:
        return
    channel_layer = get_channel_layer()
    serializer = LogSerializer(instance)

    async_to_sync(channel_layer.group_send)(
        "logs",
        {
            "type": "log_update",
            "data": serializer.data
        }
    )
