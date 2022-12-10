from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from forum.forms import PostForm, LoginForm, ForumUserForm, CommentForm
from forum.models import *


def landing_view(request, *args, **kwargs):
    context = {

    }
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'welcome.html', context)


def home_view(request, *args, **kwargs):
    sort_method = request.GET.get("sort_method")

    if not request.user.is_authenticated:
        return redirect('landing')
    if sort_method == "date":
        posts = Post.objects.all().order_by("date").reverse()
    else:
        posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')
    context = {
        'posts': posts,
        'sort_method': sort_method,
    }
    return render(request, 'home.html', context)


@login_required
def new_post_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user.forumuser
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'new_post.html', context)


# class NewPost(CreateView):
#     model = Post
#     template_name = 'new_post.html'
#     success_url = reverse_lazy('home')
#     fields = ('title', 'content', 'category', 'user')
#
#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.user = self.request.user.forumuser
#         return super().form_valid(form)


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


class PostView(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["object"]
        context['comments'] = Comment.objects.all().filter(post=post)
        return context


class BlogPostView(ListView):
    model = BlogPost
    template_name = 'blog.html'
