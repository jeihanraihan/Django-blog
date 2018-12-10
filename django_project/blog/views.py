from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author' : 'Ryan',
        'title' : 'Post 1',
        'content' : 'First content',
        'date_posted' : '6 Desember 2018'
    },
    {
        'author' : 'Wahyu',
        'title' : 'Post 2',
        'content' : 'Second content',
        'date_posted' : '7 Desember 2018'
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
