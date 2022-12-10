from django import forms
from django.contrib.auth.forms import UserCreationForm

from forum.models import Post, ForumUser, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content'
        ]
        widgets = {
            'title':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Title',
                'class':'post-title-input',
            }),
            'content':forms.Textarea(attrs={
                'placeholder':'Type here...',
                'class':'post-content-input',
            }),
            'category': forms.Select(attrs={
                'class':'post-category-input'
            })
        }



class ForumUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Username',
    })
                               )
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Password',
    })
                               )
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Confirm Password',
    })
                               )
    class Meta:
        model = ForumUser
        fields = (
            'username',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Username',
            }),
            'password1': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Password1',
            }),
            'password2': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Password2',
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Username',
    })
                               )
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Password',
    })
                               )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user',
            'post',
            'body',
            'active'
        ]