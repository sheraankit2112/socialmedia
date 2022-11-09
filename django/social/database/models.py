from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class userdata(models.Model):
    username=models.CharField(max_length=20)
    token=models.CharField(max_length=100)

class userbio(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    mobile=models.IntegerField(max_length=20)
    profile=models.ImageField(upload_to="profile")
    


class userposts(models.Model):
    username=models.CharField(max_length=20)
    post=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=30,default="None")

