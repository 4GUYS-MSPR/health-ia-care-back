from app.models.gender import Gender
from app.models.level import Level
from app.models.member import Member
from app.models.session import Session
from app.models.subscription import Subscription

from app.schemas.member import MemberScheme
from app.schemas.session import SessionScheme

from app.utils.types import AnyUser

from . import BaseAction

class SessionAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(SessionScheme, user)

    def handle(self, data: list[SessionScheme]):
        for scheme in data:

            member_scheme = MemberScheme(**scheme.model_dump())
            fields = [
                {"key": "gender", "model": Gender, "field": "value"},
                {"key": "level", "model": Level, "field": "pk"},
                {"key": "subscription", "model": Subscription, "field": "value"}
            ]
            member_data = member_scheme.model_dump()
            member_data["client"] = self.user
            for field in fields:
                v = member_data[field["key"]]
                m = field["model"].objects.get(**{field["field"]: self.upper(v) if isinstance(v, str) else v})
                member_data[field["key"]] = m

            member, _ = Member.objects.get_or_create(**member_data)

            session, _ = Session.objects.get_or_create(
                avg_bpm=scheme.avg_bpm,
                calories_burned=scheme.calories_burned,
                duration=scheme.duration,
                max_bpm=scheme.max_bpm,
                resting_bpm=scheme.resting_bpm,
                water_intake=scheme.water_intake,
                member=member
            )
            session.exercices.set(scheme.exercices)
            session.save()

        return self.success(len(data))
