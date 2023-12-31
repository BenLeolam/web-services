from django.shortcuts import render
from blogs.models import Category, Blog

def blog(request):
    
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at') 
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'pages/blogs/blog.html', context)

def blog_details(request):
    return render(request, 'pages/blogs/blog_details.html')
