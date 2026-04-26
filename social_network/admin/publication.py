from django.contrib import admin
from django.utils.html import format_html

from unfold.admin import ModelAdmin

from social_network.admin import CommentInline, LikeInline
from social_network.forms import PublicationForm
from social_network.models import Publication
from core.utils.display import display_video

class PublicationAdmin(ModelAdmin):
    form = PublicationForm

    list_display = ["pk", "display_description", "get_like_count", "type", "display_image", "display_small_video", "created_at"]
    list_filter = ["type"]
    search_fields = ["pk", "created_at"]

    def get_fields(self, request, obj=None):
        fields = ("description", "type", "image", "video", "created_at")
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
        print(dir(obj))
        return obj.like_set.count()
