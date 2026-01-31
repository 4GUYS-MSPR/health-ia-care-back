from django.db import models
from django.utils.timezone import now

from .member import Member

class Objective(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.value)
