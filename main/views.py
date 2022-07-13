from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    return render(request, 'base.html', {
        'title': 'main'
    })


def all_post(request):
    q = request.GET.get('q')
    if q is not None:
        post = Post.objects.filter(title__icontains=q)
    else:
        post = Post.objects.all()
    return render(request, 'all_post.html', {
        'title': 'main',
        'post': post,
    })


def detail(request, slug):
    p = Post.objects.get(slug=slug)
    return render(request, 'detail.html', {
        'title': 'main',
        'post': p,
    })

