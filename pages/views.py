from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')
def register(request):
    return render(request, 'pages/register.html')
def forgot_password(request):
    return render(request, 'pages/forgot_password.html')

def coming_soon(request):
    return render(request, 'pages/coming_soon.html')