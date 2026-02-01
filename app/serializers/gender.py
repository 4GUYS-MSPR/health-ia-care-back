from rest_framework import serializers

from app.models import Gender

class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ["id", "value"]
