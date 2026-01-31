from django.db import models
from django.utils.timezone import now

class Setup(models.Model):

    date = models.DateTimeField(blank=False, null=False)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.date)
