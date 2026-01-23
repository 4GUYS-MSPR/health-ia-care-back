from django.db import models

from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt

from .food_category import FoodCategory
from .meal_type import MealType

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
    meal_type = models.ForeignKey(MealType, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return str(self.label)

class FoodScheme(BaseModel):
    label: str
    calories: NonNegativeInt
    protein: NonNegativeFloat
    carbohydrates: NonNegativeFloat
    fat: NonNegativeFloat
    fiber: NonNegativeFloat
    sugars: NonNegativeFloat
    sodium: NonNegativeInt
    cholesterol: NonNegativeInt
    water_intake: NonNegativeInt

    category: str
    meal_type: str
