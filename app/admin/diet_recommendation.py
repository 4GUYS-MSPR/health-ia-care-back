from django.contrib import admin

from .allergie import AllergieInline
from .dietary_restriction import DietaryRestrictionInline

class DietRecommendationAdmin(admin.ModelAdmin):

    list_display = ["pk", "member", "create_at"]
    list_filter = [
        "member",
        "activity",
        "allergies",
        "dietary_restrictions",
        "disease_type",
        "preferred_cuisine",
        "recommendation",
        "severity",
        "create_at"
    ]

    fieldsets = [
        (None, {"fields": [
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
