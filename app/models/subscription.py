from django.db import models
from django.utils.timezone import now

class Subscription(models.Model):

    value = models.CharField(max_length=50, blank=False, null=False)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.value)

    @staticmethod
    def get_factory_values():
        return [
            "FREE",
            "PREMIUM",
            "PREMIUM PLUS",
        ]
