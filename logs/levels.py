from django.db import models

class LogLevel(models.TextChoices):
    CRITICAL = 'critical', 'CRITICAL'
    DEBUG = 'debug', 'DEBUG'
    ERROR = 'error', 'ERROR'
    INFO = 'info', 'INFO'
    SUCCESS = 'success', 'SUCCESS'
    WARNING = 'warning', 'WARNING'
