from rest_framework import serializers

from app.models import DietRecommendation

from app.serializers.activity import ActivitySerializer
from app.serializers.allergie import AllergieSerializer
from app.serializers.dietary_restriction import DietaryRestrictionSerializer
from app.serializers.disease_type import DiseaseTypeSerializer
from app.serializers.preferred_cuisine import PreferredCuisineSerializer
from app.serializers.recommendation import RecommendationSerializer
from app.serializers.severity import SeveritySerializer

class DietRecommendationSerializer(serializers.ModelSerializer):

    activity = ActivitySerializer(read_only=True)
    allergies = AllergieSerializer(many=True, read_only=True)
    dietary_restrictions = DietaryRestrictionSerializer(many=True, read_only=True)
    disease_type = DiseaseTypeSerializer(read_only=True)
    preferred_cuisine = PreferredCuisineSerializer(read_only=True)
    recommendation = RecommendationSerializer(read_only=True)
    severity = SeveritySerializer(read_only=True)

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
