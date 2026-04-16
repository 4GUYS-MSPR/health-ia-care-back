from django.contrib import admin
from django.contrib.auth import get_user_model, models

from core.admin.group import GroupAdmin
from core.admin.user import UserAdmin

admin.site.unregister(models.Group)
admin.site.register(models.Group, GroupAdmin)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
