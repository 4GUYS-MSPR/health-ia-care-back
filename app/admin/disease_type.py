from django.contrib import admin

class DiseaseTypeAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
