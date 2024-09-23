from django.shortcuts import render
from .models import article

# Create your views here.
def home(request):
    return render(request, 'blog/templates/home.html')

def blogs(request):
    articles = article.objects.all()  # Only show published posts
    return render(request, 'blog/templates/blogs.html', {'articles': articles})
    #return render(request, 'blog/templates/blogs.html')
