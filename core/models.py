from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   

    def get_absolute_url(self):
        return reverse('Blogger', args=[int(self.id)])

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    intro = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('Blog', args=[int(self.id)])

    def __str__(self):
        return self.name

class Post(models.Model):
    post_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(to=Blog, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    image = models.ImageField(verbose_name='Post image')
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250, null=True)

    def get_absolute_url(self):
        return reverse('Post', args=[int(self.id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField(default=datetime.now)
    content = models.CharField(max_length=250)
