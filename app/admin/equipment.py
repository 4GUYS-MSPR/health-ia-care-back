from unfold.admin import ModelAdmin, TabularInline

from app.models.exercice import Exercice

from core.exports import ExportCsvMixin

class EquipmentAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class EquipmentInline(TabularInline):
    model = Exercice.equipments.through
    verbose_name = "Equipment"
    verbose_name_plural = "Equipments"
    extra = 0
