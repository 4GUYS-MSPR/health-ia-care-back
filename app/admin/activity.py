from django.contrib import admin

class ActivityAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
