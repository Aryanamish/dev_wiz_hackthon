from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html', {
        'title': 'main'
    })


def all_post(request):
    return render(request, 'all_post.html', {
        'title': 'main'
    })


def detail(request):
    return render(request, 'detail.html', {
        'title': 'main'
    })

