from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar = ImageField(manual_crop='')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = ImageField()
    name = models.CharField(max_length=30)
    caption = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Comments(models.Model):
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.comment
