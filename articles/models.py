from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


