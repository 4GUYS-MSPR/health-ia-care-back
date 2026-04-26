from django.contrib import admin

from unfold.admin import ModelAdmin

from app.admin.objective import ObjectiveInline

from core.exports import ExportCsvMixin

class MemberAdmin(ExportCsvMixin, ModelAdmin):

    list_display = ["pk", "get_client_name", "age", "gender", "level", "subscription", "created_at"]
    list_filter = ["gender", "level", "subscription", "client"]
    search_fields = ["client__first_name", "client__last_name", "client__username"]

    readonly_fields = ["get_client_name"]

    fieldsets = [
        (None, {"fields": ["client", "age", "gender", "level", "subscription", "created_at"]}),
        ("Data", {"fields": ["bmi", "fat_percentage", "height", "weight", "workout_frequency"]}),
    ]

    inlines = [ObjectiveInline]

    @admin.display(description="Name")
    def get_client_name(self, obj):
        fullname = obj.client.get_full_name()
        return fullname if fullname != "" else str(obj.client.username)
