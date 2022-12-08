from django.contrib import admin

# Register your models here.

from django.contrib import admin
from forum.models import ForumUser, Post, Category


class ForumAdmin(admin.ModelAdmin):
    pass


admin.site.register(ForumUser, ForumAdmin)
admin.site.register(Post, ForumAdmin)
admin.site.register(Category, ForumAdmin)
