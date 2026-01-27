from django.contrib import admin

class RecommendationAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
