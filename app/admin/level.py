from django.contrib import admin
from app.models.level import Level

class LevelAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']