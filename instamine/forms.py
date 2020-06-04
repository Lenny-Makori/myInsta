from django import forms
from .models import Profile, Image, comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        exclude = ['user', 'image']