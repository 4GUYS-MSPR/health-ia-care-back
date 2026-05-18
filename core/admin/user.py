from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ["username", "first_name", "last_name", "is_staff", "get_member_id"]
    list_filter = ["is_staff"]

    readonly_fields = ["get_member_id"]

    @admin.display(description='Member ID')
    def get_member_id(self, obj):
        if hasattr(obj, 'member'):
            return obj.member.id
        return "-"
