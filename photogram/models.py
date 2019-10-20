from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos/',null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = HTMLField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__icontains=search_term))
        return profiles

    def save_profile(self):

        '''Method to save a profile in the database'''

        self.save()


    def update_profile(self):

        ''' Method to update a profile in the database'''

        self.update()

    def delete_profile(self):

        ''' Method to delete a profile from the database'''

        self.delete()

class Post(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=255,null=True)
    caption = models.CharField(max_length=3000)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def save_photo(self, user):
        '''Method to save an image in the database'''
        self.save()

    def update_photo(self,user):
        ''' Method to update an image in the database'''
        self.update()

    def delete_photo(self, user):
        ''' Method to delete an image from the database'''
        self.delete()

    @classmethod
    def all_photos(cls):
        all_photos = cls.objects.all()
        return all_photos

    @classmethod
    def user_photos(cls, username):
        photos = cls.objects.filter(uploaded_by__username=username)
        return photos

    @classmethod
    def filter_by_caption(cls, search_term):
        return cls.objects.filter(caption__icontains=search_term)

class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def save_comment(self):
        '''Method to save a comment in the database'''
        self.save()

    def delete_comment(self):

        ''' Method to delete a comment from the database'''
        self.delete()

class Like(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    control = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.control

    def save_like(self):
        self.save()

    @classmethod
    def num_likes(cls, post_id):
        post = Like.objects.filter(post=post_id)

   
class Follow(models.Model):
    username = models.ForeignKey(User, related_name='follower')
    followed = models.ForeignKey(User, related_name='followed')
    follow = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.follow

    def save_like(self):
        self.save()

    @classmethod
    def get_following(cls, user_id):
        following = Follow.objects.filter(user=user_id).all()
        return following
