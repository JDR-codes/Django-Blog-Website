from django.db import models
from articles.models import *
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} --> {self.comment}'

class Like(models.Model):
    post = models.OneToOneField(Article,on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.post} --> {self.like_count}'
