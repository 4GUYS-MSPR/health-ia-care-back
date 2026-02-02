from rest_framework import serializers

from app.models import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = ["id", "value"]
