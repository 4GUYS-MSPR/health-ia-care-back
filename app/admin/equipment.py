from django.contrib import admin
from app.models.exercice import Exercice

class EquipmentAdmin(admin.ModelAdmin):

    list_display = ['pk','value']
    search_fields = ['value']

class EquipmentInline(admin.TabularInline):
    model = Exercice.equipments.through
    verbose_name = "Equipment"
    verbose_name_plural = "Equipments"
    extra = 0
