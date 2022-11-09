from unittest.util import _MAX_LENGTH
from django.db import models

class data(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=20)

