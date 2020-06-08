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
    def setUp(self):
        self.new_user = User(username="food", email="heyhey@gmail.com", password="darling")
        self.new_user.save()
        self.new_profile = Profile(bio="i am tall", user=self.new_user, profile_pic="mypic.jpg")
        self.new_profile.save()
        self.image = Image(image='image.jpg', image_name='picture', image_caption='random picture', profile=self.new_profile, comments='random comment')
    