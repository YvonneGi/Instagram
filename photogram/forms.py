from django import forms
from .models import Profile,Post,Comment,Like
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['']       
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']

        
class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
        exclude=['username','post','control']

        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['upload_by', 'pub_date','likes','profile']

        
class FollowForm(forms.ModelForm):
    class Meta:
        model=Follow
        exclude=['username','followed','follow_id']