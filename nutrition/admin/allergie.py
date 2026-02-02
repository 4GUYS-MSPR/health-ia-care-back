from django.contrib import admin

from core.exports import ExportCsvMixin

from nutrition.models import DietRecommendation

class AllergieAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class AllergieInline(admin.TabularInline):
    model = DietRecommendation.allergies.through
    verbose_name = "Allergie"
    verbose_name_plural = "Allergies"
    extra = 0
