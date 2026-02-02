from rest_framework import serializers

from nutrition.models import DietRecommendation
from nutrition.serializers.activity import ActivitySerializer
from nutrition.serializers.allergie import AllergieSerializer
from nutrition.serializers.dietary_restriction import DietaryRestrictionSerializer
from nutrition.serializers.disease_type import DiseaseTypeSerializer
from nutrition.serializers.preferred_cuisine import PreferredCuisineSerializer
from nutrition.serializers.recommendation import RecommendationSerializer
from nutrition.serializers.severity import SeveritySerializer

class DietRecommendationSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['activity'] = ActivitySerializer(instance.activity).data if instance.activity else None
        rep['allergies'] = AllergieSerializer(instance.allergies, many=True).data if instance.allergies else []
        rep['dietary_restrictions'] = DietaryRestrictionSerializer(instance.dietary_restrictions, many=True).data if instance.dietary_restrictions else []
        rep['disease_type'] = DiseaseTypeSerializer(instance.disease_type).data if instance.disease_type else None
        rep['preferred_cuisine'] = PreferredCuisineSerializer(instance.preferred_cuisine).data if instance.preferred_cuisine else None
        rep['recommendation'] = RecommendationSerializer(instance.recommendation).data if instance.recommendation else None
        rep['severity'] = SeveritySerializer(instance.severity).data if instance.severity else None

        return rep

    class Meta:
        model = DietRecommendation
        fields = [
            "id",
            "adherence_to_diet_plan",
            "blood_pressure",
            "cholesterol",
            "daily_caloric_intake",
            "dietary_nutrient_imbalance_score",
            "glucose",
            "weekly_exercise_hours",
            "activity",
            "allergies",
            "dietary_restrictions",
            "disease_type",
            "member",
            "preferred_cuisine",
            "recommendation",
            "severity",
            "create_at"
        ]
        read_only_fields = ["client"]
