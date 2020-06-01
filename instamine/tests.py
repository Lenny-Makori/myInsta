from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = Profile(profile_pic='profile.jpg', bio='Big man Bazuu')

    def test_instance(self):
        self.assertTrue(isinstance(self.user, Profile))

    def test_save_method(self):
        self.user.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.user.save_profile()
        self.user.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ImageTestClass(TestCase):
    