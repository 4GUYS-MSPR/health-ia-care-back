import uuid

from app.models import Client, Gender, Level, Member, Objective, Subscription
from app.schemas.member import MemberScheme

from core.utils.logger import logger
from core.utils.types import AnyUser
from core.utils.validation import validate_fields_data
from core.utils.user import User

from . import BaseAction

class MemberAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(MemberScheme, user)

    def handle(self, data: list[MemberScheme]):
        fields = [
            {"name": "objective", "model": Objective, "is_list": False},
            {"name": "gender", "model": Gender, "is_list": False},
            {"name": "level", "model": Level, "is_list": False},
            {"name": "subscription", "model": Subscription, "is_list": False},
        ]
        invalid_value = validate_fields_data(data, fields)
        if invalid_value:
            return logger.invalid_fields(invalid_value)

        for scheme in data:

            client = Client.objects.get(code=scheme.client)
            objective = Objective.objects.get(value=self.upper(scheme.objective))
            gender = Gender.objects.get(value=self.upper(scheme.gender))
            level = Level.objects.get(value=self.upper(scheme.level))
            subscription = Subscription.objects.get(value=self.upper(scheme.subscription))

            user = User.objects.filter(username=scheme.username).first()
            if not user:
                user = User.objects.create_user(
                    username=scheme.username,
                    password=str(uuid.uuid4())
                )

            Member.objects.get_or_create(
                user=user,
                client=client,

                age=scheme.age,
                bmi=scheme.bmi,
                fat_percentage=scheme.fat_percentage,
                height=scheme.height,
                weight=scheme.weight,
                workout_frequency=scheme.workout_frequency,

                objective=objective,
                gender=gender,
                level=level,
                subscription=subscription
            )

        return self.success(len(data))
