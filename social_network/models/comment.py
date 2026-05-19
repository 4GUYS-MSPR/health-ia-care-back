from django.db import models
from django.utils import timezone

from app.models import Member

from .publication import Publication

class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="comments", null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
