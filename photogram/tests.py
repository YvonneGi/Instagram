from django.test import TestCase
from .models import Profile,Post,Follow,Comment,Like
from django.contrib.auth.models import User

# Tests for Posts model.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.fina= Profile(id=1,profile_pic = '/static/images/insta-screen.png',fullname = 'Fina',
        bio='Crazy',email='gi@gmail.com')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fina,Profile))
    # Testing Save Method
    def test_save_method(self):
        self.fina.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 1)
    # # Testing update Method   
    # def test_update(self):
    #     self.wall.save_image()
    #     image = Images.objects.filter(name = "Wall").first()
    #     update = Images.objects.filter (id=image.id).update(name = "Heaven")
    #     updated = Images.objects.filter(name = "Heaven").first()
    #     self.assertTrue(Images.name,updated.name)
    # # Testing delete Method
    # def test_delete(self):
    #     self.wall.save_photo()
    #     photo = Post.objects.filter(caption="Wall").first()
    #     delete = Post.objects.filter(id=photo.id).delete()
    #     photo = Post.objects.all()
    #     self.assertTrue(len(photo) ==0 )

