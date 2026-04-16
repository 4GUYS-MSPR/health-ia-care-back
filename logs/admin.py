import json

from django.contrib import admin

from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

from logs.models import Log

class LogAdmin(ExportCsvMixin, ModelAdmin):

    search_fields = ["message"]
    list_display = ["create_at", "type", "message"]
    list_filter = ["type"]

    readonly_fields = ["create_at", "type", "message", "formated_context"]

    fieldsets = [
        (None, {"fields": ["create_at", "type", "message"]}),
        ("Context", {"fields": ["formated_context"]})
    ]

    def formated_context(self, obj: Log):
        return json.dumps(obj.context, indent=2, ensure_ascii=False)

admin.site.register(Log, LogAdmin)
