from django.contrib import admin

from app.models.diet_recommendation import DietRecommendation

class AllergieAdmin(admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class AllergieInline(admin.TabularInline):
    model = DietRecommendation.allergies.through
    verbose_name = "Allergie"
    verbose_name_plural = "Allergies"
    extra = 0
