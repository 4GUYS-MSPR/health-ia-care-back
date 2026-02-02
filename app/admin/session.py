from django.contrib import admin

from app.admin.exercice import ExerciceInline

from core.exports import ExportCsvMixin

class SessionAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "member", "client", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake", "create_at"]
    list_filter = ["member", "client"]
    search_fields = ["pk", "member", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake"]

    fieldsets = [
        (None, {"fields": ["member", "client", "avg_bpm", "calories_burned", "duration", "max_bpm", "resting_bpm", "water_intake", "create_at"]}),
    ]

    inlines = [ExerciceInline]
