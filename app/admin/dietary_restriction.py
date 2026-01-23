from django.contrib import admin

from app.models.diet_recommendation import DietRecommendation

class DietaryRestrictionAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]

class DietaryRestrictionInline(admin.TabularInline):
    model = DietRecommendation.dietary_restrictions.through
    verbose_name = "Dietary Restriction"
    verbose_name_plural = "Dietary Restrictions"
    extra = 0
