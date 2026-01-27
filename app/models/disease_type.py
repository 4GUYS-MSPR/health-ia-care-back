from django.db import models

class DiseaseType(models.Model):

    value = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.value)
