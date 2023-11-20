from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')

def blog_details(request):
    return render(request, 'pages/blog_details.html')

def login(request):
    return render(request, 'pages/login.html')
def register(request):
    return render(request, 'pages/register.html')
def coming_soon(request):
    return render(request, 'pages/coming_soon.html')