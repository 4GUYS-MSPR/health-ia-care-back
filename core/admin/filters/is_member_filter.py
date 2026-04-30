from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class IsMemberFilter(admin.SimpleListFilter):
    title = _("member status")
    parameter_name = "is_member_filter"

    def lookups(self, request, model_admin):
        return (
            ("yes", _("Yes")),
            ("no", _("No")),
        )

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(members__isnull=False).distinct()
        if self.value() == "no":
            return queryset.filter(members__isnull=True).distinct()
        return queryset
