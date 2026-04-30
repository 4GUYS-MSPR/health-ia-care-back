from django.contrib import admin

from unfold.admin import ModelAdmin

from core.exports import ExportCsvMixin

from .member import MemberInline

class ClientAdmin(ExportCsvMixin, ModelAdmin):

    list_display = [
        "pk",
        "get_user_name",
        "code",
        "created_at",
    ]
    search_fields = [
        "pk",
        "user__user__username",
        "code",
        "created_at",
    ]

    inlines = [MemberInline]

    readonly_fields = ["get_user_name", "code"]

    fieldsets = [
        (None, {"fields": ["user", "code", "created_at"]}),
    ]

    @admin.display(description="User name")
    def get_user_name(self, obj):
        return str(obj.user.username)
