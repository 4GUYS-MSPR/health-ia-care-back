from django.contrib import admin
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['pk','value']
    search_fields = ['value']