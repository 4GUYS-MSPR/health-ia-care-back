from django.contrib import admin

from social_network.models.comment import Comment
from social_network.models.publication import Publication

from .comment import CommentAdmin, CommentInline
from .publication import PublicationAdmin

admin.site.register(Comment, CommentAdmin)
admin.site.register(Publication, PublicationAdmin)
