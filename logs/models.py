from django.db import models
from django.utils.timezone import now

from core.utils.user import User

from logs.levels import LogLevel
from logs.method import HttpMethod

class Log(models.Model):

    level = models.CharField(max_length=8, choices=LogLevel, default=LogLevel.INFO)
    method = models.CharField(max_length=8, choices=HttpMethod, default=HttpMethod.GET)
    path = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    context = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.method} {self.path}"
