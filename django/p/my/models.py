from django.db import models

class mydata(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=20)
