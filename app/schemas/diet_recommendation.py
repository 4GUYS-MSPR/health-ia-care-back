from typing import List

from pydantic import field_validator, NonNegativeFloat, NonNegativeInt

from app.models.member import Member
from app.schemas.member import PartMemberScheme

class DietRecommendationScheme(PartMemberScheme):
    adherence_to_diet_plan: NonNegativeFloat
    blood_pressure: NonNegativeInt
    cholesterol: NonNegativeFloat
    daily_caloric_intake: NonNegativeInt
    dietary_nutrient_imbalance_score: NonNegativeFloat
    glucose: NonNegativeFloat
    weekly_exercise_hours: NonNegativeFloat

    activity: str
    allergies: List[str]
    dietary_restrictions: List[str]
    disease_type: str
    preferred_cuisine: str
    recommendation: str
    severity: str

    @field_validator('allergies', 'dietary_restrictions', mode='before')
    @classmethod
    def split_comma_string(cls, v):
        if isinstance(v, list):
            return [item for item in v if str(item).strip().upper() != "NONE"]
        if isinstance(v, str):
            return [item.strip() for item in v.split(';') if item.strip() and item.strip().upper() != "NONE"]
        return v

class ValidDietRecommendationScheme(DietRecommendationScheme):

    member: Member

    class Config:
        arbitrary_types_allowed = True
