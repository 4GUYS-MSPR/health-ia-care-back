from django.contrib import admin

from app.models.exercice import Exercice

class MuscleAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]

class TargetMuscleInline(admin.TabularInline):
    model = Exercice.target_muscles.through
    verbose_name = "Target Muscle"
    verbose_name_plural = "Target Muscles"
    extra = 0

class SecondaryMuscleInline(admin.TabularInline):
    model = Exercice.secondary_muscles.through
    verbose_name = "Secondary Muscle"
    verbose_name_plural = "Secondary Muscles"
    extra = 0
