from django.contrib import admin

class SeverityAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
