# Create your models here.
from django.contrib.humanize.templatetags import humanize
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone


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
        return reverse("category", kwargs={"pk": self.pk})


class Post(models.Model):
    category = models.ManyToManyField(Category, related_name="categories", blank=True)
    user = models.ForeignKey(ForumUser, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=90)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(ForumUser, related_name="likes", blank=True)

    def get_date(self):
        return humanize.naturaltime(self.date)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})


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

    def get_date(self):
        return humanize.naturaltime(self.created_on)


class Therapist(models.Model):
    specialties = (
        ('Psychotherapy', 'Psychotherapy'),
        ('Economics', 'Economics'),
    )

    area = models.TextField(choices=specialties)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    day_available = models.DateField()
    bio = models.TextField()


class Hotline(models.Model):
    name = models.CharField(max_length=128, blank=False)
    address = models.TextField()
    number = models.CharField(max_length=24)


class BlogPost(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=90)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def get_date(self):
        return humanize.naturaltime(self.date)

    class Meta:
        verbose_name = "blogpost"
        verbose_name_plural = "blogpost"

    def get_absolute_url(self):
        return reverse("blogpost", kwargs={"pk": self.pk})

    def delete(self, *args, **kwargs):
        self.image.storage.delete(self.image.name)
        return super().delete(*args, **kwargs)
