from django.shortcuts import render
from .models import Blog, Post, Writer
# from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def recents(request):
    blogs = Blog.objects.all()
    posts = Post.objects.all()
    return render(request, 'core/recent_posts.html', context={'blogs': blogs, 'posts': posts})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'core/blogs.html', context={'blogs': blogs})

def bloggers(request):
    bloggers = Writer.objects.all()
    return render(request, 'core/bloggers.html', context={'bloggers': bloggers})

def blogger(request, pk):
    blogger = Writer.objects.filter(pk=pk)
    user = blogger[0].user
    blogs = Blog.objects.filter(author=user)
    return render(request, 'core/blogger.html', context={'blogger': blogger, 'blogs': blogs, 'user': user})

def post(request, pk):
    post = Post.objects.filter(pk=pk)[0]
    return render(request, 'core/post.html', context={'post': post})

def blog(request, pk):
    blog = Blog.objects.filter(pk=pk)[0]
    posts = Post.objects.filter(source=blog)
    return render(request, 'core/blog.html', context={'blog': blog, 'posts': posts})
