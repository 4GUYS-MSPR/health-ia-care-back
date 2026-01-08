from django.db import models

class Equipment(models.Model):
    value = models.CharField(max_length=255, blank=False, null=False)
