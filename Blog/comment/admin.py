from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'article', 'created_time', 'parent_comment']
    fields = ['name', 'email', 'text', 'article', 'reply_name', 'parent_comment']


admin.site.register(Comment, CommentAdmin)