from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='https://img.icons8.com/nolan/64/user-default.png',upload_to='profile_pictures')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username