from pydantic import BaseModel, NonNegativeFloat, NonNegativeInt

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
