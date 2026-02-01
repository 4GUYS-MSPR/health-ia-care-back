from django.contrib import messages
from django.utils.safestring import mark_safe

from admin_extra_buttons.mixins import ExtraButtonsMixin
from admin_extra_buttons.decorators import button

class ExportCsvMixin(ExtraButtonsMixin):

    @button(
        label = mark_safe('<style>li{list-style: none;}</style><i class="fas fa-file-csv"></i> Exporter'),
        html_attrs = {
            "class": "btn btn-primary",
        }
    )
    def export_as_csv(self, request):
        messages.info(request, f"Model: {self.model.__name__}")
