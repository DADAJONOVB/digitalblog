from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'status','publish',]
    list_filter = ['status','created','publish','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status','publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created','active']
    list_filter = ['active','created','author']
    search_fields = ['author','body']
