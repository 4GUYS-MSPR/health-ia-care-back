from rest_framework import serializers

from app.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ["id", "value"]
