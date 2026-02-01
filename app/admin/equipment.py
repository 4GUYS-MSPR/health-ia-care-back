from django.contrib import admin

from app.exports import ExportCsvMixin
from app.models.exercice import Exercice

class EquipmentAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class EquipmentInline(admin.TabularInline):
    model = Exercice.equipments.through
    verbose_name = "Equipment"
    verbose_name_plural = "Equipments"
    extra = 0
