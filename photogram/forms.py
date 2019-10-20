from django import forms
from .models import Profile,Post,Comment,Like
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['owner']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =['likes','profile']

        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']

        
class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
        exclude=['username','post','control']