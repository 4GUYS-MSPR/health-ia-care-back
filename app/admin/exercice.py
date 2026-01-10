from django.contrib import admin
from django.utils.html import format_html

from app.admin.body_part import BodyPartInline
from app.admin.equipment import EquipmentInline
from app.admin.muscle import TargetMuscleInline, SecondaryMuscleInline
from app.models.session import Session

from app.admin.body_part import BodyPartInline
from app.admin.equipment import EquipmentInline

class ExerciceAdmin(admin.ModelAdmin):

    list_display = ['pk', 'category', 'display_image']
    list_filter = ['category']

    readonly_fields = ['display_image', 'display_image_large']

    search_fields = ['pk', 'category__value', 'image_url']

    fieldsets = [
        (None, {"fields": ["display_image_large", "category"]}),
    ]

    inlines = [
        EquipmentInline,
        BodyPartInline,
        TargetMuscleInline,
        SecondaryMuscleInline,
    ]

    def display_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 2px;" />', obj.image_url)
        return "No image"

    display_image.short_description = 'Image'
    
    def display_image_large(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 300px; height: auto; border-radius: 2px;" />', obj.image_url)
        return "No image"

    display_image_large.short_description = 'Image'

class ExerciceInline(admin.TabularInline):
    model = Session.exercices.through
    verbose_name = 'Exercice'
    verbose_name_plural = 'Exercices'
    extra = 0

    fields = ['get_pk', 'get_category', 'get_image']
    readonly_fields = ['get_pk', 'get_category', 'get_image']

    def get_pk(self, instance):
        return instance.exercice.pk
    get_pk.short_description = 'Pk'

    def get_category(self, instance):
        return instance.exercice.category
    get_category.short_description = 'Category'

    def get_image(self, instance):
        if instance.exercice.image_url:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 2px;" />', instance.exercice.image_url)
        return "No image"
    get_image.short_description = 'Image'
