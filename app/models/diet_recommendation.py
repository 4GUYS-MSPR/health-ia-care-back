from django.db import models

from .activity import Activity
from .allergie import Allergie
from .dietary_restriction import DietaryRestriction
from .disease_type import DiseaseType
from .member import Member
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
