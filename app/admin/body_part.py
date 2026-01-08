from django.contrib import admin
from app.models.body_part import BodyPart

class BodyPartAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']