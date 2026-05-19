from unfold.admin import ModelAdmin, TabularInline

from social_network.models import Comment

class CommentAdmin(ModelAdmin):
    list_display = ["pk", "member", "content", "created_at"]
    search_fields = ["pk", "created_at"]

    fields = ["publication", "member", "content", "created_at"]

class CommentInline(TabularInline):
    tab = True
    model = Comment
    verbose_name = "Comment"
    verbose_name_plural = "Comments"
    extra = 0
