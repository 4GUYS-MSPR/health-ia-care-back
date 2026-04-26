from unfold.admin import ModelAdmin, TabularInline

from social_network.models import Like

class LikeAdmin(ModelAdmin):
    list_display = ["pk", "member", "created_at"]
    search_fields = ["pk", "created_at"]

    fields = ["member", "publication", "created_at"]

class LikeInline(TabularInline):
    tab = True
    model = Like
    verbose_name = "Like"
    verbose_name_plural = "Likes"
    extra = 0
