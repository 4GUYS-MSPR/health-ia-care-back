from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

class FoodAdmin(ExportCsvMixin, ModelAdmin):

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
