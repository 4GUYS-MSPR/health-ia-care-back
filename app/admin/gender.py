from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

class GenderAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
