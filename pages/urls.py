from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home.html'),

    path('about', views.about, name='about.html'),

    path('blog', views.blog, name='blog.html'),
    path('blog_details', views.blog_details, name='blog_details.html'),

    path('login', views.login, name='login.html'), 
    path('register', views.register, name='register'),

    path('coming_soon', views.coming_soon, name='coming_soon' ),
]