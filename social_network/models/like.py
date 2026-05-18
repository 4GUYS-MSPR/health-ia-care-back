from django.db import models
from django.utils import timezone

from app.models import Member

from .publication import Publication

class Like(models.Model):

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(default=timezone.now)
