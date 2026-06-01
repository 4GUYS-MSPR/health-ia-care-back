from django.db import models
from django.utils.timezone import now

class Training(models.Model):
    members = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Train over {str(self.members)} members at {str(self.created_at)}"
