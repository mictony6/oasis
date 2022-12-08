from django import forms

from forum.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content',
        ]
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'centered',
        #         'placeholder': 'Post Title'
        #     }),
        #     'category': forms.SelectMultiple(attrs={
        #         'class': 'centered',
        #     }),
        #
        #
        #     'investment': forms.NumberInput(attrs={
        #         'placeholder': '₱PHP'
        #     }),
        #     'details': forms.Textarea(attrs={
        #         'class': 'details',
        #         'placeholder': 'Type out specifics here.'
        #     })
        #
        # }