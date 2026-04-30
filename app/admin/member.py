from django.contrib import admin

from unfold.admin import ModelAdmin, TabularInline

from app.models import Member
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
        "client__user__username",
        "user__user__username",
    ]

    readonly_fields = ["get_client_name", "get_user_name"]

    fieldsets = [
        (None, {"fields": ["user", "client", "age", "gender", "level", "subscription", "last_activity", "created_at"]}),
        ("Data", {"fields": ["bmi", "fat_percentage", "height", "weight", "workout_frequency"]}),
    ]

    inlines = [ObjectiveInline]

    @admin.display(description="Client name")
    def get_client_name(self, obj):
        return str(obj.client.user.username)

    @admin.display(description="User name")
    def get_user_name(self, obj):
        return str(obj.user.username)

class MemberInline(TabularInline):
    model = Member
    verbose_name = "Member"
    verbose_name_plural = "Members"
    extra = 0
