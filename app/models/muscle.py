from django.db import models

class Muscle(models.Model):
    value = models.CharField(max_length=255, blank=False, null=False)
