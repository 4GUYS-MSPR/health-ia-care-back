from django.contrib import admin

from unfold.admin import ModelAdmin

from logs.models import Log

class LogAdmin(ModelAdmin):
    list_display = ["pk", "level", "method", "path", "user"]
    list_filter = ["level", "method"]
    search_fields = ["level", "method", "pk", "user", "path"]

admin.site.register(Log, LogAdmin)
