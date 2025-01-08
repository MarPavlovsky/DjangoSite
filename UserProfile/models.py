from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Friends(models.Model):
    name = models.CharField(
        max_length=20,
        null=True
    )
    def __str__(self):
        return self.name


class BIO(models.Model):
    bio = models.TextField()
    def __str__(self):
        return self.bio
    
class MyProfile(models.Model):
    friends = models.ManyToManyField(Friends)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    bio = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
