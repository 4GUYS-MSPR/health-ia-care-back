from uuid import uuid4

from django.db import models
from django.utils.timezone import now

from core.utils.user import User

class Client(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client',
    )
    uuid = models.CharField(
        max_length=100,
        default=uuid4,
        unique=True,
        editable=False,
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user.username)
