from django.contrib import admin

from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.client import Client
from app.models.equipment import Equipment
from app.models.exercice import Exercice
from app.models.gender import Gender
from app.models.level import Level
from app.models.member import Member
from app.models.muscle import Muscle
from app.models.session import Session
from app.models.subscription import Subscription

from app.admin.body_part import BodyPartAdmin
from app.admin.category import CategoryAdmin
from app.admin.client import ClientAdmin
from app.admin.equipment import EquipmentAdmin
from app.admin.exercice import ExerciceAdmin
from app.admin.gender import GenderAdmin
from app.admin.level import LevelAdmin
from app.admin.muscle import MuscleAdmin
from app.admin.member import MemberAdmin
from app.admin.session import SessionAdmin
from app.admin.subscription import SubscriptionAdmin

admin.site.register(BodyPart, BodyPartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Muscle, MuscleAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
