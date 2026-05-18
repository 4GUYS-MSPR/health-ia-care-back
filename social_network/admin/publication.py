from django.contrib import admin
from django.utils.html import format_html

from unfold.admin import ModelAdmin

from social_network.admin.comment import CommentInline
from social_network.admin.like import LikeInline
from social_network.forms import PublicationForm
from social_network.models.publication import Publication
from core.utils.display import display_video

class PublicationAdmin(ModelAdmin):
    form = PublicationForm

    list_display = ["pk", "get_user_name", "display_description", "get_like_count", "type", "display_image", "display_small_video", "created_at"]
    list_filter = ["type"]

    readonly_fields = ["get_user_name"]
    search_fields = ["pk", "created_at"]

    def get_fields(self, request, obj=None):
        fields = ("user", "description", "type", "image", "video", "created_at")
        if obj:
            fields += ("display_large_video",)
        return fields

    readonly_fields = [
        "display_description",
        "display_image",
        "display_small_video",
        "display_large_video",
        "get_like_count"
    ]
    inlines = [CommentInline, LikeInline]

    @admin.display(description="User name")
    def get_user_name(self, obj):
        return str(obj.user.username)

    @admin.display(description="Description")
    def display_description(self, obj: Publication):
        if len(obj.description) > 100:
            return obj.description[:97] + "..."
        return obj.description

    @admin.display(description="Image")
    def display_image(self, obj: Publication):
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height: auto; border-radius: 2px;" />', obj.image.url)
        return "No image"

    @admin.display(description="Video preview")
    def display_small_video(self, obj: Publication):
        return display_video(100, obj.video)

    @admin.display(description="Video preview")
    def display_large_video(self, obj: Publication):
        return display_video(300, obj.video)

    @admin.display(description="Likes")
    def get_like_count(self, obj: Publication):
        return obj.likes.count()
