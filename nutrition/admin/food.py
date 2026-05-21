from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

class FoodAdmin(ModelAdmin, ExportCsvMixin):

    list_display = [
        "pk",
        "label",
        "category",
        "meal_type",
        "create_at",
    ]
    list_filter = ["category", "meal_type"]

    search_fields = ["label"]

    fieldsets = [
        (None, {"fields": ["label", "category", "meal_type", "create_at"]}),
        ("Data", {"fields": [
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "fiber",
            "sugars",
            "sodium",
            "cholesterol",
            "water_intake",
        ]})
    ]
