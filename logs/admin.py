from django.contrib import admin

from .models import Log

class LogAdmin(admin.ModelAdmin):

    search_fields = ["message"]
    list_display = ["create_at", "type", "message"]
    list_filter = ["type"]

    fieldsets = [
        (None, {"fields": ["create_at", "type", "message"]}),
        ("Context", {"fields": ["context"]})
    ]

admin.site.register(Log, LogAdmin)
