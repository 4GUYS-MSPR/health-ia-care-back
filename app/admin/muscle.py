from django.contrib import admin

from app.exports import ExportCsvMixin
from app.models.exercice import Exercice

class MuscleAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
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
