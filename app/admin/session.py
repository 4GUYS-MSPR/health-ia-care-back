from django.contrib import admin
from app.models.session import Session

class SessionAdmin(admin.ModelAdmin):
    list_display =['avg_bpm', 'calories_burned', 'duration', 'max_bpm', 'resting_bpm', 'water_intake']
    list_filter =['avg_bpm', 'calories_burned', 'duration', 'max_bpm', 'resting_bpm', 'water_intake']