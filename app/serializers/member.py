from rest_framework import serializers

from app.models import Member

from app.serializers.gender import GenderSerializer
from app.serializers.level import LevelSerializer
from app.serializers.objective import ObjectiveSerializer
from app.serializers.subscription import SubscriptionSerializer

class MemberSerializer(serializers.ModelSerializer):

    objectives = ObjectiveSerializer(many=True, required=False)

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['gender'] = GenderSerializer(instance.gender).data if instance.gender else None
        rep['level'] = LevelSerializer(instance.level).data if instance.level else None
        rep['subscription'] = SubscriptionSerializer(instance.subscription).data if instance.subscription else None
        rep['objectives'] = ObjectiveSerializer(instance.objectives, many=True).data if instance.objectives else []

        return rep

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
            "created_at"
        ]
        read_only_fields = ["client"]
