from django.urls import path
from forum.views import home_view, new_post_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('new/', new_post_view, name='new_post'),
    path('about/', about_view, name='about'),
]
