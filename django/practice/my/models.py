from django.db import models

class userdata(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    profile=models.ImageField(upload_to="profile")

class userpost(models.Model):
    username=models.CharField(max_length=20)
    post=models.ImageField(upload_to="post")
