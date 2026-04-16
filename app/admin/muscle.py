from unfold.admin import ModelAdmin, TabularInline

from app.models.exercice import Exercice

from core.exports import ExportCsvMixin

class MuscleAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class TargetMuscleInline(TabularInline):
    model = Exercice.target_muscles.through
    verbose_name = "Target Muscle"
    verbose_name_plural = "Target Muscles"
    extra = 0

class SecondaryMuscleInline(TabularInline):
    model = Exercice.secondary_muscles.through
    verbose_name = "Secondary Muscle"
    verbose_name_plural = "Secondary Muscles"
    extra = 0
