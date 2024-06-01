from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post
from .models import About
def posts(request):
    posts = Post.objects.filter(status=1)  
    return render(request, 'index.html', {'posts': posts})
def post_detail(request, pk):
    about=About.objects.all()
    post = get_object_or_404(Post, pk=pk)
    posts= Post.objects.filter(status=1)
    return render(request, 'post_detail.html', {'post': post,'about':about,'posts':posts})

def abput(request):
    about=About.objects.all()
    return render(request, 'about.html',{'about': about})