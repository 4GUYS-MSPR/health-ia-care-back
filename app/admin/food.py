from django.contrib import admin

from app.exports import ExportCsvMixin
from app.models.exercice import Exercice

class FoodAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = [
        "pk",
        "label",
        "category",
        "meal_type",
        "create_at",
        "client"
    ]
    list_filter = ["category", "meal_type", "client"]

    search_fields = ["label"]

    fieldsets = [
        (None, {"fields": ["label", "category", "meal_type", "client", "create_at"]}),
        ("Data", {"fields": [
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "fiber",
            "sugars",
            "sodium",
            "cholesterol",
            "water_intake"
        ]})
    ]

class FoodInline(admin.TabularInline):
    model = Exercice.body_parts.through
    verbose_name = "Food"
    verbose_name_plural = "Foods"
    extra = 0
