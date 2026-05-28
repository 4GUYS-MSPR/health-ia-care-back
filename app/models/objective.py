from django.db import models
from django.utils.timezone import now

class Objective(models.Model):

    value = models.CharField(max_length=20, blank=False, null=False)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.value)
