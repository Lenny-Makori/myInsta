from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.TextField()