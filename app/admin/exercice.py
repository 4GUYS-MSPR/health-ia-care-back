from django.contrib import admin
from django.utils.html import format_html

from app.admin.body_part import BodyPartInline
from app.admin.equipment import EquipmentInline
from app.admin.muscle import TargetMuscleInline, SecondaryMuscleInline
from app.exports import ExportCsvMixin
from app.models.session import Session

class ExerciceAdmin(ExportCsvMixin, admin.ModelAdmin):

    list_display = ["pk", "category", "display_image", "client", "create_at"]
    list_filter = ["category", "client"]

    readonly_fields = ["display_image", "display_image_large"]

    search_fields = ["pk", "category__value", "image_url"]

    fieldsets = [
        (None, {"fields": ["display_image_large", "category", "client", "create_at"]}),
    ]

    inlines = [
        EquipmentInline,
        BodyPartInline,
        TargetMuscleInline,
        SecondaryMuscleInline,
    ]

    @admin.display(description="Image")
    def display_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 2px;" />', obj.image_url)
        return "No image"

    @admin.display(description="Image")
    def display_image_large(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 300px; height: auto; border-radius: 2px;" />', obj.image_url)
        return "No image"

class ExerciceInline(admin.TabularInline):
    model = Session.exercices.through
    verbose_name = 'Exercice'
    verbose_name_plural = 'Exercices'
    extra = 0

    fields = ['get_pk', 'get_category', 'get_image']
    readonly_fields = ['get_pk', 'get_category', 'get_image']

    @admin.display(description="Pk")
    def get_pk(self, instance):
        return instance.exercice.pk

    @admin.display(description="Category")
    def get_category(self, instance):
        return instance.exercice.category

    @admin.display(description="Image")
    def get_image(self, instance):
        if instance.exercice.image_url:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 2px;" />', instance.exercice.image_url)
        return "No image"
