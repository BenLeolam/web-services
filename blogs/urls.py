from django.urls import path 
from . import views 

urlpatterns = [
    path('blog', views.blog, name='blog.html'),
    path('blog_details', views.blog_details, name='blog_details.html'),
]