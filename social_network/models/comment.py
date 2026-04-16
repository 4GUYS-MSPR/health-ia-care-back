from django.db import models
from django.utils import timezone

from .publication import Publication

class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
