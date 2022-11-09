from django.db import models

class studentdata(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
