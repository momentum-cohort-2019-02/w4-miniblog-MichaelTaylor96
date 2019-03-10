from django.contrib import admin
from .models import Blog, Post, Comment

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
