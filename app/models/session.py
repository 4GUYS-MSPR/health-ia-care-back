from django.db import models

from datetime import time
from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import List

from .exercice import Exercice
from .member import Member

class Session(models.Model):

    avg_bpm = models.IntegerField()
    calories_burned = models.FloatField()
    duration = models.TimeField()
    max_bpm = models.IntegerField()
    resting_bpm = models.IntegerField()
    water_intake = models.FloatField()

    exercices = models.ManyToManyField(Exercice, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session {self.pk}"

class SessionScheme(BaseModel):
    abg_bpm: PositiveInt
    calories_burned: PositiveFloat
    duration: time
    max_bpm: PositiveInt
    resting_bpm: PositiveInt
    water_intake: PositiveFloat
    exercices: List[PositiveInt]
    member: PositiveInt
