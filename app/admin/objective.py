from django.contrib import admin

from app.models.objective import Objective

class ObjectiveInline(admin.TabularInline):
    model = Objective
    verbose_name = "Objective"
    verbose_name_plural = "Objectives"
    extra = 1
