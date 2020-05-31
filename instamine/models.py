from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)