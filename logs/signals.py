from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Log
from .serializers import LogSerializer

@receiver(post_save, sender=Log)
def announce_task_update(sender, instance, **kwargs): # pylint: disable=unused-argument
    channel_layer = get_channel_layer()
    serializer = LogSerializer(instance)
    
    async_to_sync(channel_layer.group_send)(
        "tasks",
        {
            "type": "task_update",
            "data": serializer.data
        }
    )

@receiver(post_delete, sender=Log)
def task_deleted_handler(sender, instance: Log, **kwargs): # pylint: disable=unused-argument
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "logs",
        {
            "type": "task_update",
            "data": {
                "action": "deleted",
                "id": instance.pk,
            }
        }
    )
