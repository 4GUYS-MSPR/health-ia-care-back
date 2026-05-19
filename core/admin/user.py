from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from core.utils.user import User

from .avatar import AvatarInline

class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ["display_image", "username", "first_name", "last_name", "is_staff", "get_member_id"]
    list_filter = ["is_staff"]

    readonly_fields = ["display_image", "get_member_id"]

    inlines = [AvatarInline]

    @admin.display(description='Member ID')
    def get_member_id(self, obj):
        if hasattr(obj, 'member'):
            return obj.member.id
        return "-"

    @admin.display(description="Avatar")
    def display_image(self, obj: User):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 40px; height: auto; border-radius: 2px;" />', obj.avatar.value.url)
        return "-"
