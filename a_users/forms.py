from .models import *
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile #access the profile table 
        exclude = ['user']
        labels = {
            'realname': 'Name'
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows':3})
            
        }
