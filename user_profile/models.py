from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/')
    bio = models.TextField(null=True)
    followers = models.ManyToManyField(User, related_name='followers')
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    