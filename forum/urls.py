import django.contrib.auth
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from forum.views import *

urlpatterns = [
    path('', landing_view, name="landing"),
    path('home/', home_view, name='home'),
    path('new/', new_post_view, name='new_post'),
    path('about/', about_view, name='about'),
    path('counselling/', counselling_view, name='counselling'),
    path('login/', login_view, name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('blog/', BlogPostView.as_view(), name='blog'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)