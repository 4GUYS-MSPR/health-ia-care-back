from rest_framework import serializers

from app.models import Gender

class ObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ["id", "value"]
