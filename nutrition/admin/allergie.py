from unfold.admin import ModelAdmin, TabularInline

from core.exports import ExportCsvMixin

from nutrition.models import DietRecommendation

class AllergieAdmin(ModelAdmin, ExportCsvMixin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class AllergieInline(TabularInline):
    model = DietRecommendation.allergies.through
    verbose_name = "Allergie"
    verbose_name_plural = "Allergies"
    extra = 0
