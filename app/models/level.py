from django.db import models

class Level(models.Model):
    value = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.value
