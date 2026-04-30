from django.db import models

from .member import Member

class MemberLastActivity(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('member', 'date')
