from django import forms
from .models import Profile,Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['owner']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =['likes','profile']