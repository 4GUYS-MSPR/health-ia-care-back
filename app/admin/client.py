from django.contrib import admin

from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

from .member import MemberInline

class ClientAdmin(ExportCsvMixin, ModelAdmin):

    list_display = [
        "pk",
        "get_user_name",
        "uuid",
        "created_at",
    ]
    search_fields = [
        "pk",
        "user__user__username",
        "uuid",
        "created_at",
    ]

    inlines = [MemberInline]

    readonly_fields = ["get_user_name", "uuid"]

    fieldsets = [
        (None, {"fields": ["user", "uuid", "created_at"]}),
    ]

    @admin.display(description="User name")
    def get_user_name(self, obj):
        return str(obj.user.username)
