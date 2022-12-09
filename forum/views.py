from django.shortcuts import get_object_or_404, redirect, render

from forum.forms import PostForm
# Create your views here.
from forum.models import Post


def home_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all(),
    }
    print(context['posts'][0].date)
    return render(request, 'home.html', context)


def new_post_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)


def about_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'about.html', context)


def counselling_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'counselling.html', context)
