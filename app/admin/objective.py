from unfold.admin import TabularInline

from app.models.objective import Objective

class ObjectiveInline(TabularInline):
    model = Objective
    verbose_name = "Objective"
    verbose_name_plural = "Objectives"
    extra = 1
