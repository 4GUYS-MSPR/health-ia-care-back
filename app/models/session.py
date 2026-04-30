from django.db import models
from django.utils.timezone import now

from .client import Client
from .exercice import Exercice
from .member import Member

class Session(models.Model):

    avg_bpm = models.IntegerField()
    calories_burned = models.FloatField()
    duration = models.TimeField()
    max_bpm = models.IntegerField()
    resting_bpm = models.IntegerField()
    water_intake = models.FloatField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    exercices = models.ManyToManyField(Exercice, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Session {self.pk}"
