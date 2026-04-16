from unfold.admin import ModelAdmin, TabularInline

from core.exports import ExportCsvMixin

from nutrition.models import DietRecommendation

class DietaryRestrictionAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class DietaryRestrictionInline(TabularInline):
    model = DietRecommendation.dietary_restrictions.through
    verbose_name = "Dietary Restriction"
    verbose_name_plural = "Dietary Restrictions"
    extra = 0
