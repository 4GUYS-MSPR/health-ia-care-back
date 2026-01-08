from django.contrib import admin
class LevelAdmin(admin.ModelAdmin):
    list_display = ['pk','value']
    search_fields = ['value']