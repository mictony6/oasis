# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class ForumUser(User):
    class Meta:
        verbose_name = "forumuser"
        verbose_name_plural = "forumusers"

    def get_absolute_url(self):
        return reverse("forumuser_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    category = models.ManyToManyField(Category, related_name="categories", blank=True)
    user = models.ForeignKey(ForumUser, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=90)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(ForumUser, related_name="likes", blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.get_username())

