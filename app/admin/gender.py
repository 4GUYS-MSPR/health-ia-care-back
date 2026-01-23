from django.contrib import admin

class GenderAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
