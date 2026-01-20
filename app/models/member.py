from django.db import models
from django.contrib.auth.models import User

from pydantic import BaseModel, field_validator, PositiveFloat, PositiveInt

from .gender import Gender
from .level import Level
from .subscription import Subscription

class Member(models.Model):

    age = models.PositiveIntegerField(null=True)
    bmi = models.FloatField()
    fat_percentage = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    workout_frequency = models.IntegerField()

    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name='genders')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='levels')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, related_name='subscriptions')

    def get_client_name(self):
        fullname = self.client.get_full_name()
        return fullname if fullname != "" else str(self.client.username)

    def __str__(self):
        return self.get_client_name()

class MemberScheme(BaseModel):
    age: PositiveInt
    bmi: PositiveFloat
    fat_percentage: PositiveFloat
    height: PositiveFloat
    weight: PositiveFloat
    workout_frequency: PositiveInt

    gender: str = "NOT SPECIFIED"
    level: int
    subscription: str = "FREE"

    @field_validator("gender")
    @classmethod
    def check_gender(cls, v: str):
        return v if v != "" else "NOT SPECIFIED"
