from django.db import models

from .gender import Gender
from .level import Level
from .subscription import Subscription

class Member(models.Model):
    bmi = models.FloatField()
    fat_percentage = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    workout_frequency = models.IntegerField()

    gender = models.ForeignKey(Gender, on_delete=models.SET_DEFAULT, default='NOT SPECIFIED',related_name='genders')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='levels')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, related_name='subscriptions')
