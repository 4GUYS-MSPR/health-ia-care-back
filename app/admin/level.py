from django.contrib import admin

from app.exports import ExportCsvMixin

class LevelAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
