from django.contrib import admin

class PreferredCuisineAdmin(admin.ModelAdmin):

    list_display = ['pk','value']
    search_fields = ['value']
