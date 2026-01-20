from django.contrib import admin

from app.models.exercice import Exercice

class MeetTypeAdmin(admin.ModelAdmin):

    list_display = ['pk','value']
    search_fields = ['value']

class MeetTypeInline(admin.TabularInline):
    model = Exercice.body_parts.through
    verbose_name = "Meet Type"
    verbose_name_plural = "Meet Types"
    extra = 0
