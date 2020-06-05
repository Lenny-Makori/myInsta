from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='image/', default="image/male.png", blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.bio

    @classmethod
    def get_profile(cls, user_id):
        profile = cls.objects.get(user=user_id)
        return profile

    @classmethod
    def search_by_username(cls, search_term):
        username = User
        searched_user = cls.objects.filter(username__icontains=search_term)

        return searched_user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_image_of_user(cls, user_id):
        image = cls.objects.filter(profile=user_id)

        return image


class comment(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    @classmethod
    def display_comments(cls, image_id):
        comments = cls.objects.filter(image=image_id)

        return comments