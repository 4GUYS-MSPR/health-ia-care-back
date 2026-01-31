from django.contrib import admin

class PreferredCuisineAdmin(admin.ModelAdmin):

    list_display = ["pk", "value", "create_at"]
    search_fields = ["value"]
