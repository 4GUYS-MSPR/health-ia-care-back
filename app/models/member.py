from django.db import models


class Member(models.Model):
    gender = models.CharField(max_length=10) #enum
    weight = models.FloatField()
    height = models.FloatField()
    fat_percentage = models.FloatField()
    workout_frequency = models.IntegerField()
    experience_level = models.CharField(max_length=10) #enum
    bmi = models.FloatField()
    subscription_type = models.CharField(max_length=20) #enum

    

    