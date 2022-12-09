from django.contrib import admin

# Register your models here.

from django.contrib import admin
from forum.models import ForumUser, Post, Category, Comment, Therapist, Hotline


@admin.register(ForumUser)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content', 'date')
    list_filter = ('user', 'date', 'category')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'area', 'day_available', 'bio')
    list_filter = ('area', 'day_available')
    search_fields = ('name', 'area')


@admin.register(Hotline)
class HotlinAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'number')
    search_fields = ('name', 'address')
