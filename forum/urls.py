from django.urls import path
from forum.views import home_view, new_post_view

urlpatterns= [
    path('', home_view, name='home'),
    path('new/', new_post_view, name='new_post')
]