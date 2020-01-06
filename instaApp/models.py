from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = ImageField(manual_crop='')
    bio = models.CharField(max_length=200)

class Image(models.Model):
    image = ImageField()
    name = models.CharField(max_length=30)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

class Comments(models.Model):
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(Profile)
