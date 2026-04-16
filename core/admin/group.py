from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from unfold.admin import ModelAdmin

class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
