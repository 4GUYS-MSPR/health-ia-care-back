from django.db import models
from django.utils.timezone import now

from app.utils.client_code import gen_client_code

from core.utils.user import User

class Client(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client',
    )
    code = models.CharField(
        max_length=6,
        default=gen_client_code,
        unique=True,
        editable=False,
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user.username)
