from django.contrib import admin
from . models import Category, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    ordering = ['id']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author', 'created_at', 'category']
    ordering = ['id']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)