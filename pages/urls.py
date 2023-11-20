from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home.html'),

    path('about', views.about, name='about.html'),

    path('login', views.login, name='login.html'), 
    path('register', views.register, name='register'),
    path('forgot-password', views.forgot_password, name='forgot_password'),

    path('coming_soon', views.coming_soon, name='coming_soon' ),
]