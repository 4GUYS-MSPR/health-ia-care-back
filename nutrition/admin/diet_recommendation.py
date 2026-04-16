from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

from nutrition.admin.allergie import AllergieInline
from nutrition.admin.dietary_restriction import DietaryRestrictionInline

class DietRecommendationAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "member", "client", "create_at"]
    list_filter = [
        "member",
        "activity",
        "allergies",
        "dietary_restrictions",
        "disease_type",
        "preferred_cuisine",
        "recommendation",
        "severity",
        "create_at",
        "client"
    ]

    fieldsets = [
        (None, {"fields": [
            "client",
            "member",
            "activity",
            "disease_type",
            "preferred_cuisine",
            "recommendation",
            "severity"
        ]}),
        ("Data", {"fields": [
            "adherence_to_diet_plan",
            "blood_pressure",
            "cholesterol",
            "daily_caloric_intake",
            "dietary_nutrient_imbalance_score",
            "glucose",
            "weekly_exercise_hours"
        ]})
    ]

    inlines = [AllergieInline, DietaryRestrictionInline]
