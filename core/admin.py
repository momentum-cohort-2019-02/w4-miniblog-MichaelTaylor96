from django.contrib import admin
from .models import Blog, Post, Comment, Writer

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

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass
