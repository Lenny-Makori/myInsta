from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='image/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user

    @classmethod
    def get_profile(cls, user_id):
        profile = cls.objects.get(user=user_id)
        return profile

    @classmethod
    def search_by_username(cls, search_term):
        username = User
        searched_user = cls.objects.filter(username__icontains=search_term)

        return searched_user


class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)