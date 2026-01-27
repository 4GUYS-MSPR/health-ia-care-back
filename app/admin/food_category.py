from django.contrib import admin

from app.models.exercice import Exercice

class FoodCategoryAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]

class FoodCategoryInline(admin.TabularInline):
    model = Exercice.body_parts.through
    verbose_name = "Food Category"
    verbose_name_plural = "Food Categories"
    extra = 0
