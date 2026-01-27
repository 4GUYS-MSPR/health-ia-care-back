from django.contrib import admin

class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ["pk", "value"]
    search_fields = ["value"]
