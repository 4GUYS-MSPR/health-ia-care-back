from django.db import models

from .member import Member

class Objective(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)
