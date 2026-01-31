from django.db import models
from django.utils.timezone import now

class Log(models.Model):

    class LogType(models.TextChoices):
        CRITICAL = 'critical', 'CRITICAL'
        DEBUG = 'debug', 'DEBUG'
        ERROR = 'error', 'ERROR'
        INFO = 'info', 'INFO'
        SUCCESS = 'success', 'SUCCESS'
        WARNING = 'warning', 'WARNING'

    create_at = models.DateTimeField(default=now)
    context = models.JSONField(max_length=2000, default=dict)
    message = models.CharField(max_length=500)
    type = models.CharField(max_length=8, choices=LogType, default=LogType.INFO)

    def __str__(self):
        return str(self.message)
