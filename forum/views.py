from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forum.forms import PostForm, LoginForm, ForumUserForm
from forum.models import Post, Therapist, Hotline


def landing_view(request, *args, **kwargs):
    context = {

    }
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'welcome.html', context)


def home_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('landing')
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)


def new_post_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('landing')
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
    if not request.user.is_authenticated:
        return redirect('landing')
    context = {
        'therapists': Therapist.objects.all(),
        'hotlines': Hotline.objects.all(),
    }
    return render(request, 'counselling.html', context)


def login_view(request, *args, **kwargs):
    form = LoginForm()
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'

                return redirect('home')
            else:
                message = 'Login failed!'

    context = {'form': form, 'message': message}
    return render(request, 'login.html', context)


class UserLogoutView(LogoutView):
    template_name = "welcome.html"
    extra_context = None


class UserCreateView(CreateView):
    form_class = ForumUserForm
    template_name = "register.html"
    success_url = reverse_lazy('login')
