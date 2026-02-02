from rest_framework import serializers

from nutrition.models import Activity

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ["id", "value"]
