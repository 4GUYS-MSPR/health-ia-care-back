from django.contrib import messages

from admin_extra_buttons.mixins import ExtraButtonsMixin
from admin_extra_buttons.decorators import button

class ExportCsvMixin(ExtraButtonsMixin):

    @button(
        label="Exporter en CSV",
        html_attrs = {
            "style": "background-color: green; color: white;"
        }
    )
    def export_as_csv(self, request):
        messages.info(request, f"Model: {self.model.__name__}")
