from django.contrib import admin

class ExerciceAdmin(admin.ModelAdmin):

    list_display = ['pk','image_url', 'category']
    list_filter = ['category', 'equipments' ]
