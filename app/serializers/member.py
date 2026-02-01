from rest_framework import serializers

from app.models import Member

from app.serializers.gender import GenderSerializer
from app.serializers.level import LevelSerializer
from app.serializers.objective import ObjectiveSerializer
from app.serializers.subscription import SubscriptionSerializer

class MemberSerializer(serializers.ModelSerializer):

    gender = GenderSerializer(read_only=True)
    level = LevelSerializer(read_only=True)
    objectives = ObjectiveSerializer(many=True, read_only=True)
    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = Member
        fields = [
            "id",
            "age",
            "bmi",
            "fat_percentage",
            "height",
            "weight",
            "workout_frequency",
            "objectives",
            "gender",
            "level",
            "subscription",
            "create_at"
        ]
