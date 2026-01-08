from django.db import models

from .exercice import Exercice
from .member import Member

class Session(models.Model):

    avg_bpm = models.IntegerField()
    calories_burned = models.FloatField()
    duration = models.TimeField()
    max_bpm = models.IntegerField()
    resting_bpm = models.IntegerField()
    water_intake = models.FloatField()

    exercices = models.ManyToManyField(Exercice, blank=True, related_name='exercices')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='members')
