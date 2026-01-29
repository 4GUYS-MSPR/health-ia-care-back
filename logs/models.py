from django.db import models
from django.utils.timezone import now

LogType = [
    ('critical', 'CRITICAL'),
    ('debug', 'DEBUG'),
    ('error', 'ERROR'),
    ('info', 'INFO'),
    ('success', 'SUCCESS'),
    ('warning', 'WARNING'),
]

class Log(models.Model):

    create_at = models.DateTimeField(default=now)
    context = models.JSONField(max_length=2000, default=dict)
    message = models.CharField(max_length=500)
    type = models.CharField(max_length=8, choices=LogType, default='info')

    def __str__(self):
        return str(self.message)
