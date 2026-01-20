from datetime import time
from typing import List

from django.db import models

from pydantic import field_validator, PositiveFloat, PositiveInt

from .exercice import Exercice
from .member import Member, MemberScheme

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

class SessionScheme(MemberScheme):
    avg_bpm: PositiveInt
    calories_burned: PositiveFloat
    duration: time
    max_bpm: PositiveInt
    resting_bpm: PositiveInt
    water_intake: PositiveFloat
    exercices: List[PositiveInt] = []

    @field_validator("duration", mode="before")
    @classmethod
    def convert_duration(cls, v):
        if isinstance(v, time):
            return v

        if isinstance(v, str):
            v = v.strip()
            if v == "":
                raise ValueError("Duration is empty")
            try:
                v = float(v)
            except ValueError as exc:
                raise ValueError("Invalid duration format") from exc

        if isinstance(v, (float, int)):
            total_seconds = int(v * 3600)
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return time(hour=hours, minute=minutes, second=seconds)

        raise ValueError("Invalid duration format")
