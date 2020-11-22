from django import forms
from .models import Image, Profile,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['posted_by','date_posted', 'image_likes']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']