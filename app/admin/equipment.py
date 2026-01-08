from django.contrib import admin
from app.models.equipment import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']