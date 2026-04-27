from rest_framework import serializers

from social_network.models import Like

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
