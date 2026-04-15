from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

class PreferredCuisineAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
