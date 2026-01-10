from django.contrib import admin

from app.admin.exercice import ExerciceInline

class SessionAdmin(admin.ModelAdmin):

    list_display =["pk", "member", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake"]
    search_fields = ["pk", "member", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake"]

    fieldsets = [
        (None, {"fields": ["member", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake"]}),
    ]

    inlines = [ExerciceInline]
