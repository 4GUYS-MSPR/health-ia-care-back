from django.contrib import admin

from core.exports import ExportCsvMixin

class PreferredCuisineAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
