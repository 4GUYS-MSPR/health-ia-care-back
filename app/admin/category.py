from django.contrib import admin
from app.models.category import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']