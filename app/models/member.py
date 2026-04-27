from django.db import models
from django.utils.timezone import now

from core.utils.user import User

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="members")
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="clients")
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name='genders')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='levels')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, related_name='subscriptions')

    created_at = models.DateTimeField(default=now)
    last_activity = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
