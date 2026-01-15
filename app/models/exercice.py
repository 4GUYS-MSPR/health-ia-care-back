from typing import List
from urllib.parse import urlparse

from django.db import models
from pydantic import BaseModel, field_validator

from .body_part import BodyPart
from .category import Category
from .equipment import Equipment
from .muscle import Muscle

class Exercice(models.Model):

    image_url = models.URLField()

    body_parts = models.ManyToManyField(BodyPart, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='categories')
    equipments = models.ManyToManyField(Equipment, blank=True, related_name='equipments')
    secondary_muscles = models.ManyToManyField(Muscle, blank=True, related_name='secondary_muscles')
    target_muscles = models.ManyToManyField(Muscle, blank=True, related_name='target_muscles')

    def __str__(self):
        return f"Exercice {self.pk}"

class ExerciceScheme(BaseModel):
    imageUrl: str

    bodyParts: List[str]
    exerciseType: str
    equipments: List[str]
    secondaryMuscles: List[str]
    targetMuscles: List[str]

    @field_validator("imageUrl")
    @staticmethod
    def check_url(_, v):
        result = urlparse(v)
        if not (result.scheme and result.netloc):
            raise ValueError(f"{v} is not a valid URL")
        return v
