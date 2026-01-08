from django.contrib import admin
from app.models.gender import Gender

class GenderAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']