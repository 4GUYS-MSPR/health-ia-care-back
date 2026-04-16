from django.db import models
from django.utils.timezone import now

from core.utils.user import User

from .body_part import BodyPart
from .category import Category
from .equipment import Equipment
from .muscle import Muscle

class Exercice(models.Model):

    image_url = models.URLField()

    body_parts = models.ManyToManyField(BodyPart, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='categories')
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    equipments = models.ManyToManyField(Equipment, blank=True, related_name='equipments')
    secondary_muscles = models.ManyToManyField(Muscle, blank=True, related_name='secondary_muscles')
    target_muscles = models.ManyToManyField(Muscle, blank=True, related_name='target_muscles')

    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Exercice {self.pk}"
