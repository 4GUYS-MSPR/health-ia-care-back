from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

class RecommendationAdmin(ModelAdmin, ExportCsvMixin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
