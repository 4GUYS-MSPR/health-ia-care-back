from django.contrib import admin

from social_network.models.comment import Comment
from social_network.models.like import Like
from social_network.models.publication import Publication

from .comment import CommentAdmin, CommentInline
from .like import LikeAdmin, LikeInline
from .publication import PublicationAdmin

admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Publication, PublicationAdmin)
