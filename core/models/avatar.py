from django.db import models

from core.utils.media import get_avatar_path
from core.utils.user import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    value = models.ImageField(
        upload_to=get_avatar_path,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.user.username)
