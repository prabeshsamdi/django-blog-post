from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post
def posts(request):
    posts = Post.objects.filter(status=1)  
    return render(request, 'index.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})