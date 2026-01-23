from typing import List

from django.db import models

from pydantic import field_validator, NonNegativeFloat, NonNegativeInt

from .activity import Activity
from .allergie import Allergie
from .dietary_restriction import DietaryRestriction
from .disease_type import DiseaseType
from .member import Member, PartMemberScheme
from .preferred_cuisine import PreferredCuisine
from .recommendation import Recommendation
from .severity import Severity

class DietRecommendation(models.Model):
    adherence_to_diet_plan = models.FloatField()
    blood_pressure = models.IntegerField()
    cholesterol = models.FloatField()
    daily_caloric_intake = models.IntegerField()
    dietary_nutrient_imbalance_score = models.FloatField()
    glucose = models.FloatField()
    weekly_exercise_hours = models.FloatField()

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    allergies = models.ManyToManyField(Allergie, blank=True)
    dietary_restrictions = models.ManyToManyField(DietaryRestriction, blank=True)
    disease_type = models.ForeignKey(DiseaseType, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    preferred_cuisine = models.ForeignKey(PreferredCuisine, on_delete=models.SET_NULL, null=True)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.SET_NULL, null=True)
    severity = models.ForeignKey(Severity, on_delete=models.SET_NULL, null=True)

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
