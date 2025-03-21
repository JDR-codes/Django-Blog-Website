from django.contrib import admin
from . models import Comment, Like
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'comment', 'created_at']
    ordering = ['id']

class LikeAdmin(admin.ModelAdmin):
    list_display =['id', 'post', 'like_count']
    ordering = ['id']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)
