from django.db import models
from django.contrib.auth.models import User

from .gender import Gender
from .level import Level
from .subscription import Subscription

class Member(models.Model):

    bmi = models.FloatField()
    fat_percentage = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    workout_frequency = models.IntegerField()

    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_DEFAULT, default='NOT_SPECIFIED', related_name='genders')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name='levels')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, related_name='subscriptions')

    def get_client_name(self):
        fullname = self.client.get_full_name()
        return fullname if fullname != "" else str(self.client.username)

    def __str__(self):
        return self.get_client_name()
