from django.contrib import admin
from app.models.exercice import Exercice

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ['image_url', 'category']
    list_filter = ['category', 'equipments' ]

