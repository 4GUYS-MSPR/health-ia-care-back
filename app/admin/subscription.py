from django.contrib import admin
from app.models.subscription import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']