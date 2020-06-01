from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.TextField()

    def __str__(self):
        return self.user

    


class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)