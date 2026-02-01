from app.models.food_category import FoodCategory
from app.models.food import Food
from app.models.meal_type import MealType

from app.schemas.food import FoodScheme

from app.utils.logger import logger
from app.utils.types import AnyUser
from app.utils.validation import validate_fields_data

from . import BaseAction

class FoodAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(FoodScheme, user)

    def handle(self, data: list[FoodScheme]):
        fields = [
            {"name": "category", "model": FoodCategory, "is_list": False},
            {"name": "meal_type", "model": MealType, "is_list": False},
        ]
        invalid_value = validate_fields_data(data, fields)
        if invalid_value:
            return logger.invalid_fields(invalid_value)

        for scheme in data:

            category = FoodCategory.objects.get(value=self.upper(scheme.category))
            meal_type = MealType.objects.get(value=self.upper(scheme.meal_type))

            Food.objects.get_or_create(
                label = scheme.label,
                calories = scheme.calories,
                protein = scheme.protein,
                carbohydrates = scheme.carbohydrates,
                fat = scheme.fat,
                fiber = scheme.fiber,
                sugars = scheme.sugars,
                sodium = scheme.sodium,
                cholesterol = scheme.cholesterol,
                water_intake = scheme.water_intake,

                category=category,
                meal_type=meal_type,

                client=self.user,
            )

        return self.success(len(data))
