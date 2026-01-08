from django.contrib import admin
from app.models.member import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['bmi', 'fat_percentage', 'height', 'weight', 'workout_frequency', 'gender', 'level', 'subscription']
    list_filter =['gender', 'level', 'subscription']
