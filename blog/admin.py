from django.contrib import admin
from blog.models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views')
    search_fields = ('title', 'content')
    list_filter = ('tags', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'is_approved')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
