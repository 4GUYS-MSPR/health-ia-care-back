from django.contrib import admin

from nutrition.models.activity import Activity
from nutrition.models.allergie import Allergie
from nutrition.models.category import Category
from nutrition.models.diet_recommendation import DietRecommendation
from nutrition.models.dietary_restriction import DietaryRestriction
from nutrition.models.disease_type import DiseaseType
from nutrition.models.food import Food
from nutrition.models.meal_type import MealType
from nutrition.models.preferred_cuisine import PreferredCuisine
from nutrition.models.recommendation import Recommendation
from nutrition.models.severity import Severity

from nutrition.admin.activity import ActivityAdmin
from nutrition.admin.allergie import AllergieAdmin
from nutrition.admin.category import CategoryAdmin
from nutrition.admin.diet_recommendation import DietRecommendationAdmin
from nutrition.admin.dietary_restriction import DietaryRestrictionAdmin
from nutrition.admin.disease_type import DiseaseTypeAdmin
from nutrition.admin.food import FoodAdmin
from nutrition.admin.meal_type import MealTypeAdmin
from nutrition.admin.preferred_cuisine import PreferredCuisineAdmin
from nutrition.admin.recommendation import RecommendationAdmin
from nutrition.admin.severity import SeverityAdmin

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Allergie, AllergieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DietRecommendation, DietRecommendationAdmin)
admin.site.register(DietaryRestriction, DietaryRestrictionAdmin)
admin.site.register(DiseaseType, DiseaseTypeAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(MealType, MealTypeAdmin)
admin.site.register(PreferredCuisine, PreferredCuisineAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Severity, SeverityAdmin)
