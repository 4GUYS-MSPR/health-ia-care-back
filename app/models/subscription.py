from django.db import models

class Subscription(models.Model):

    value = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.value)
