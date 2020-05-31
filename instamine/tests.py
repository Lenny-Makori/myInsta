from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = Profile(profile_pic='profile.jpg', bio='Big man Bazuu')

    def test_instance(self):
        self.assertTrue(isinstance(self.user, Profile))