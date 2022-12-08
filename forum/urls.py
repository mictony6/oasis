from django.urls import path
from forum.views import home_view

urlpatterns= [
    path('', home_view, name='home'),
]