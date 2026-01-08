from django.contrib import admin
class MuscleAdmin(admin.ModelAdmin):
    list_display = ['pk','value']
    search_fields = ['value']