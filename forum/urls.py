import django.contrib.auth
from django.urls import path
from forum.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', landing_view, name="landing"),
    path('home/', home_view, name='home'),
    path('new/', new_post_view, name='new_post'),
    path('about/', about_view, name='about'),
    path('counselling/', counselling_view, name='counselling'),
    path('login/', login_view, name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
