from django.contrib import admin
from app.models.muscle import Muscle

class MuscleAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']