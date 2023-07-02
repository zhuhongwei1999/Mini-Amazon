from django.contrib.auth.models import User
from django.db import models


def profile_image_path(instance, filename):
    return f"avatars/{instance.user.username}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    ups_account = models.CharField(max_length=50, default="", blank=True)
    bank_account = models.CharField(max_length=50, default="", blank=True)
    default_x = models.IntegerField(default=-1, blank=True)
    default_y = models.IntegerField(default=-1, blank=True)
    points = models.FloatField(default=0.0)
    avatar = models.ImageField(upload_to=profile_image_path, default='avatars/panda.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'

