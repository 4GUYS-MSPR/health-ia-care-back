import csv

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
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
    def export_as_csv(self, request: HttpRequest):
        try:
            now = timezone.now().strftime("%Y-%m-%d_%Hh%M")
            filename = f"{self.model.__name__.lower()}_export_{now}.csv"
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            writer = csv.writer(response)
            queryset = self.model.objects.all()
        
            fields = [field.name for field in self.model._meta.fields]
            writer.writerow(fields)

            for obj in queryset:
                writer.writerow([getattr(obj, field) for field in fields])

            return response

        except Exception as e:
            messages.error(request, f"Can't export to csv for model {self.model.__name__}: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER', '..'))
