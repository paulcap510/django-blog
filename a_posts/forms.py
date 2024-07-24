from django.forms import ModelForm
from django import forms

from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'artist', 'url', 'image', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add caption...',
                'class': 'font1 text-4xl'
            }),
            'url': forms.TextInput(attrs={'placeholder': 'Add URL...'}),
            'image': forms.TextInput(attrs={'placeholder': 'Add Image URL...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Add Title...'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Add Artist...'})
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'artist', 'url', 'image', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add caption...',
                'class': 'font1 text-4xl'
            }),
            'url': forms.TextInput(attrs={'placeholder': 'Add URL...'}),
            'image': forms.TextInput(attrs={'placeholder': 'Add Image URL...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Add Title...'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Add Artist...'})
        }