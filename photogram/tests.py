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
        self.fina= Profile(id=1,profile_pic = '/static/images/insta-screen.png',fullname = 'Fina',
        bio='Crazy',email='gi@gmail.com')
        self.fina.save_user_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 1)
    # Testing update Method   
    # def test_update(self):
    #     self.fina.save_user_profile(self)
    #     profile = Profile.objects.filter(fullname = "Fina").first()
    #     update = Profile.objects.filter (id=profile.id).update(fullname = "Anna")
    #     updated = Profile.objects.filter(fullname = "Anna").first()
    #     self.assertTrue(updated.fullname)
    # # # Testing delete Method
    # def test_delete(self):
    #     self.fina.save_user_profile(self)
    #     username = Profile.objects.filter(fullname="Fina").first()
    #     delete = Profile.objects.filter(id=username.id).delete()
    #     username = Profile.objects.all()
    #     self.assertTrue(len(username) ==0 )


# Tests for Follow model.
# class FollowTestClass(TestCase):
#     # Set up method
#     def setUp(self):
#         self.1= Follow(follow = '1')
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.1,Follow))
    # Testing Save Method
    # def test_save_method(self):
    #     self.car.save_category()
    #     categories = Category.objects.all()
    #     self.assertTrue(len(categories) > 0)

