from django.contrib import admin

from app.admin.body_part import BodyPartInline
from app.admin.equipment import EquipmentInline

class ExerciceAdmin(admin.ModelAdmin):

    list_display = ['pk', 'category', 'image_url']
    list_filter = ['category']

    search_fields = ['pk', 'category__value', 'image_url']

    fieldsets = [
        (None, {"fields": ["image_url", "category"]}),
    ]
    
    inlines = [EquipmentInline, BodyPartInline]
    # secondary_muscles
    # target_muscles
