from django.db import models
from django.utils.timezone import now

from app.models import Client

from nutrition.models.category import Category
from nutrition.models.meal_type import MealType

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

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    meal_type = models.ForeignKey(MealType, null=True, on_delete=models.SET_NULL)

    create_at = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return str(self.label)
