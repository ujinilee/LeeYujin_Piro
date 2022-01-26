from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'like']
    list_display_links = ['title', 'like']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'content'
    ]
