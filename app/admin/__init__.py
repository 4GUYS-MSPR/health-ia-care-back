from django.contrib import admin

from app.models.member import Member
from app.models.exercice import Exercice
from app.models.session import Session
from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.food import Food
from app.models.food_category import FoodCategory
from app.models.gender import Gender
from app.models.level import Level
from app.models.meal_type import MealType
from app.models.muscle import Muscle
from app.models.subscription import Subscription

from app.admin.member import MemberAdmin
from app.admin.exercice import ExerciceAdmin
from app.admin.session import SessionAdmin
from app.admin.body_part import BodyPartAdmin
from app.admin.category import CategoryAdmin
from app.admin.equipment import EquipmentAdmin
from app.admin.food import FoodAdmin
from app.admin.food_category import FoodCategoryAdmin
from app.admin.gender import GenderAdmin
from app.admin.level import LevelAdmin
from app.admin.meal_type import MealTypeAdmin
from app.admin.muscle import MuscleAdmin
from app.admin.subscription import SubscriptionAdmin

admin.site.register(Member, MemberAdmin)
admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(BodyPart, BodyPartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Muscle, MuscleAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
