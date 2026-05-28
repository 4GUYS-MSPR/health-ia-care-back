from django.db import models
from django.utils.timezone import now

from core.utils.user import User

from .client import Client
from .objective import Objective
from .gender import Gender
from .level import Level
from .subscription import Subscription

class Member(models.Model):

    age = models.PositiveIntegerField(null=True)
    bmi = models.FloatField(default=0)
    fat_percentage = models.FloatField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    workout_frequency = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name="members")
    objective = models.ForeignKey(Objective, on_delete=models.SET_NULL, null=True, related_name='objective')
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name='gender')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='level')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, related_name='subscription')

    created_at = models.DateTimeField(default=now)
    last_activity = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
