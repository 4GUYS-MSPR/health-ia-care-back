from django.contrib import admin

from app.models.exercice import Exercice

from core.exports import ExportCsvMixin

class BodyPartAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]

class BodyPartInline(admin.TabularInline):
    model = Exercice.body_parts.through
    verbose_name = "Body part"
    verbose_name_plural = "Body parts"
    extra = 0
