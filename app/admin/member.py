from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):

    list_display = ['pk', 'bmi', 'fat_percentage', 'height', 'weight', 'workout_frequency', 'gender', 'level', 'subscription']
    list_filter =['gender', 'level', 'subscription']
