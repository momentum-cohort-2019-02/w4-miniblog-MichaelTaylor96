from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('recents/', views.recents, name='Recents'),
    path('blogs/', views.blogs, name='Blogs'),
    path('bloggers/', views.bloggers, name='Bloggers'),
    path('bloggers/<int:pk>/', views.blogger, name='Blogger')
]
