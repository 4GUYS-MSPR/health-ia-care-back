from django.db import models

class FoodCategory(models.Model):

    value = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.value)
