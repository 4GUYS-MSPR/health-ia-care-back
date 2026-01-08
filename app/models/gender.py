from django.db import models

class Gender(models.Model):
    value = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.value
