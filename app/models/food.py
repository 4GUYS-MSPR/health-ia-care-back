from django.db import models

from pydantic import BaseModel, PositiveFloat, PositiveInt

from .food_category import FoodCategory
from .meet_type import MeetType

class Food(models.Model):
    label = models.CharField(max_length=50)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fat = models.FloatField()
    fiber = models.FloatField()
    sugars = models.FloatField()
    sodium = models.IntegerField()
    cholesterol = models.IntegerField()
    water_intake = models.IntegerField()

    category = models.ForeignKey(FoodCategory, null=True, on_delete=models.SET_NULL)
    meal_type = models.ForeignKey(MeetType, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return str(self.label)

class FoodScheme(BaseModel):
    label: str
    calories: PositiveInt
    protein: PositiveFloat
    carbohydrates: PositiveFloat
    fat: PositiveFloat
    fiber: PositiveFloat
    sugars: PositiveFloat
    sodium: PositiveInt
    cholesterol: PositiveInt
    water_intake: PositiveInt

    category: str
    meal_type: str
