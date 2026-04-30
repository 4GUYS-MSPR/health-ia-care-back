from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from core.utils.user import User
from .filters import IsMemberFilter

class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ["username", "first_name", "last_name", "is_member", "is_staff"]
    list_filter = [IsMemberFilter, "is_staff"]
    readonly_fields = ["is_member"]

    @admin.display(description="Is Member ?", boolean=True)
    def is_member(self, obj: User):
        return hasattr(obj, 'member')
