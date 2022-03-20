from email.policy import default
from django.db import models
# from blog.models import Post
# Create your models here.

class Post(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    slug = models.CharField(max_length=100,default=True)

    def __str__(self):
        return self.title