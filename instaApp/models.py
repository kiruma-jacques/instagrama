from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    avatar = ImageField(manual_crop='')
    bio = models.CharField(max_length=200)

class Image(models.Model):
    image = ImageField()
    iname = models.CharField(max_length=30)
    icaption = models.TextField(blank=True)
    iprofile = models.ForeignKey(Profile)
    ilikes = models.IntegerField(default=0)
    
class Comments(models.Model):
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(Profile)
