from django.shortcuts import render
from .models import Blog, Post, Blogger
from django.contrib.auth.models import User

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
    bloggers = Blogger.objects.all()
    return render(request, 'core/bloggers.html', context={'bloggers': bloggers})

def blogger(request, pk):
    blogger = Blogger.objects.filter(pk=pk)
    blogs = Blog.objects.filter(author=blogger)
    return render(request, 'core/blogger.html', context={"blogger": blogger, 'blogs': blogs})
