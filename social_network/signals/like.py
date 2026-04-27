from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from social_network.models import Like
from social_network.serializers import LikeSerializer

@receiver(post_save, sender=Like)
def announce_like_update(sender, instance, **kwargs): # pylint: disable=unused-argument
    channel_layer = get_channel_layer()
    serializer = LikeSerializer(instance)

    async_to_sync(channel_layer.group_send)(
        "likes",
        {
            "type": "like_update",
            "data": serializer.data
        }
    )
