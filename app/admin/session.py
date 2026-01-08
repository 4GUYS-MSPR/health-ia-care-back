from django.contrib import admin
class SessionAdmin(admin.ModelAdmin):
    list_display =['pk', 'avg_bpm', 'calories_burned', 'duration', 'max_bpm', 'resting_bpm', 'water_intake']
    list_filter =['avg_bpm', 'calories_burned', 'duration', 'max_bpm', 'resting_bpm', 'water_intake']