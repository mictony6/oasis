from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from forum.models import Post


def home_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all()
    }
    print(context)
    return render(request, 'home.html', context)
