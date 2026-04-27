from django.contrib import admin

from unfold.admin import ModelAdmin

from app.admin.objective import ObjectiveInline

from core.exports import ExportCsvMixin

class MemberAdmin(ExportCsvMixin, ModelAdmin):

    list_display = [
        "pk",
        "get_user_name",
        "get_client_name",
        "age",
        "gender",
        "level",
        "subscription",
        "last_activity",
        "created_at",
    ]
    list_filter = ["gender", "level", "subscription", "client"]
    search_fields = [
        "client__first_name",
        "client__last_name",
        "client__username",
        "user__first_name",
        "user__last_name",
        "user__username",
    ]

    readonly_fields = ["get_client_name", "get_user_name"]

    fieldsets = [
        (None, {"fields": ["user", "client", "age", "gender", "level", "subscription", "last_activity", "created_at"]}),
        ("Data", {"fields": ["bmi", "fat_percentage", "height", "weight", "workout_frequency"]}),
    ]

    inlines = [ObjectiveInline]

    @admin.display(description="Name")
    def get_client_name(self, obj):
        fullname = obj.client.get_full_name()
        return fullname if fullname != "" else str(obj.client.username)

    @admin.display(description="Name")
    def get_user_name(self, obj):
        fullname = obj.user.get_full_name()
        return fullname if fullname != "Anonymous" else str(obj.user.username)
