from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post
def posts(request):
    posts = Post.objects.filter(status=1)  
    return render(request, 'index.html', {'posts': posts})
