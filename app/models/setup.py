from django.db import models

class Setup(models.Model):

    date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return str(self.date)
