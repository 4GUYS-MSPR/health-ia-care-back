from rest_framework import serializers

from app.models import Activity

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ["id", "value"]
