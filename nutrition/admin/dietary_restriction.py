from django.contrib import admin

from core.exports import ExportCsvMixin

from nutrition.models import DietRecommendation

class DietaryRestrictionAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class DietaryRestrictionInline(admin.TabularInline):
    model = DietRecommendation.dietary_restrictions.through
    verbose_name = "Dietary Restriction"
    verbose_name_plural = "Dietary Restrictions"
    extra = 0
