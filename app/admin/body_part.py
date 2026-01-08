from django.contrib import admin

class BodyPartAdmin(admin.ModelAdmin):

    list_display = ['pk','value']
    search_fields = ['value']
