from django.contrib import admin

from app.models.exercice import Exercice

class MealTypeAdmin(admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class MealTypeInline(admin.TabularInline):
    model = Exercice.body_parts.through
    verbose_name = "Meal Type"
    verbose_name_plural = "Meal Types"
    extra = 0
