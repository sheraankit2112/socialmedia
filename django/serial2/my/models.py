from django.db import models

class userdata(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()


