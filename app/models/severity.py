from django.db import models
from django.utils.timezone import now

class Severity(models.Model):

    value = models.CharField(max_length=255, blank=False, null=False)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.value)
