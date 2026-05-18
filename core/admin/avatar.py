from unfold.admin import StackedInline

from core.models import Avatar

class AvatarInline(StackedInline):
    model = Avatar
    fields = ["value"]
    can_delete = False
    verbose_name_plural = "Avatar"
