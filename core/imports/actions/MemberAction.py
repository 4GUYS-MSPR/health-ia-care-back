from app.models import Gender, Level, Member, Subscription
from app.schemas.member import MemberScheme

from core.utils.logger import logger
from core.utils.types import AnyUser
from core.utils.validation import validate_fields_data

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
            return logger.invalid_fields(invalid_value)

        for scheme in data:

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

        return self.success(len(data))
