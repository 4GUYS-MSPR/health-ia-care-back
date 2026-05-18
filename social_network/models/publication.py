from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from core.utils.media import get_image_path, get_video_path
from core.utils.user import User

from social_network.validations import validate_video

class Publication(models.Model):
    class Type(models.IntegerChoices):
        IMAGE = 1, 'Image'
        VIDEO = 2, 'Vidéo'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publications")
    description = models.TextField(max_length=1000, default="")

    type = models.PositiveSmallIntegerField(
        choices=Type
    )
    image = models.ImageField(
        upload_to=get_image_path,
        null=True,
        blank=True
    )
    video = models.FileField(
        validators=[validate_video],
        upload_to=get_video_path,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.type == self.Type.IMAGE and not self.image:
            raise ValidationError({'image': "Image required"})

        if self.type == self.Type.VIDEO and not self.video:
            raise ValidationError({'video': "Video required"})
