from django.contrib import admin

from app.models.activity import Activity
from app.models.allergie import Allergie
from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.diet_recommendation import DietRecommendation
from app.models.dietary_restriction import DietaryRestriction
from app.models.disease_type import DiseaseType
from app.models.equipment import Equipment
from app.models.exercice import Exercice
from app.models.food_category import FoodCategory
from app.models.food import Food
from app.models.gender import Gender
from app.models.level import Level
from app.models.meal_type import MealType
from app.models.member import Member
from app.models.muscle import Muscle
from app.models.preferred_cuisine import PreferredCuisine
from app.models.recommendation import Recommendation
from app.models.session import Session
from app.models.severity import Severity
from app.models.subscription import Subscription

from app.admin.activity import ActivityAdmin
from app.admin.allergie import AllergieAdmin
from app.admin.body_part import BodyPartAdmin
from app.admin.category import CategoryAdmin
from app.admin.diet_recommendation import DietRecommendationAdmin
from app.admin.dietary_restriction import DietaryRestrictionAdmin
from app.admin.disease_type import DiseaseTypeAdmin
from app.admin.equipment import EquipmentAdmin
from app.admin.exercice import ExerciceAdmin
from app.admin.food_category import FoodCategoryAdmin
from app.admin.food import FoodAdmin
from app.admin.gender import GenderAdmin
from app.admin.level import LevelAdmin
from app.admin.meal_type import MealTypeAdmin
from app.admin.muscle import MuscleAdmin
from app.admin.member import MemberAdmin
from app.admin.preferred_cuisine import PreferredCuisineAdmin
from app.admin.recommendation import RecommendationAdmin
from app.admin.session import SessionAdmin
from app.admin.severity import SeverityAdmin
from app.admin.subscription import SubscriptionAdmin

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Allergie, AllergieAdmin)
admin.site.register(BodyPart, BodyPartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DietRecommendation, DietRecommendationAdmin)
admin.site.register(DietaryRestriction, DietaryRestrictionAdmin)
admin.site.register(DiseaseType, DiseaseTypeAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Muscle, MuscleAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(PreferredCuisine, PreferredCuisineAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Severity, SeverityAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
