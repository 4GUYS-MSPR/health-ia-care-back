from django.contrib import admin

class SeverityAdmin(admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
