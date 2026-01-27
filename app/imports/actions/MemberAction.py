from app.models.gender import Gender
from app.models.level import Level
from app.models.member import Member, MemberScheme
from app.models.subscription import Subscription

from app.utils.response import JsonResponse
from app.utils.types import AnyUser
from app.utils.validation import validate_fields_data

from . import BaseAction

class MemberAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(MemberScheme, user)

    def handle(self, data: list[MemberScheme]):
        fields = [
            {"name": "Gender", "model": Gender, "is_list": False},
            {"name": "Experience_Level", "model": Level, "is_list": False},
            {"name": "subscription", "model": Subscription, "is_list": False},
        ]
        invalid_value = validate_fields_data(data, fields)
        if invalid_value:
            return JsonResponse.errors({"fields": invalid_value})

        for scheme in data:
            from loguru import logger
            logger.debug(scheme.model_dump())

            gender = Gender.objects.get(value=self.upper(scheme.gender))
            level = Level.objects.get(pk=scheme.level)
            subscription = Subscription.objects.get(value=self.upper(scheme.subscription))

            Member.objects.get_or_create(
                age=scheme.age,
                bmi=scheme.bmi,
                fat_percentage=scheme.fat_percentage,
                height=scheme.height,
                weight=scheme.weight,
                workout_frequency=scheme.workout_frequency,
                client=self.user,
                gender=gender,
                level=level,
                subscription=subscription
            )

        return JsonResponse.success({"message": f"{len(data)} row{'s' if len(data) > 1 else ''} imported !"})
