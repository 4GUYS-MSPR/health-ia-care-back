from django.contrib import admin

from app.admin.allergie import AllergieInline
from app.admin.dietary_restriction import DietaryRestrictionInline
from app.exports import ExportCsvMixin

class DietRecommendationAdmin(ExportCsvMixin, admin.ModelAdmin):

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
