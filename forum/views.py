from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {
    }
    return render(request, 'home.html', context)
