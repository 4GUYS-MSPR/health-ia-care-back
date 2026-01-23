from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
