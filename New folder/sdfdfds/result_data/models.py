from django.db import models
from matplotlib import widgets

class studentBio(models.Model):
    uid=models.CharField(null=False,unique=True,max_length=20,default='2139')
    name=models.CharField(null=False,max_length=20)
    father_name=models.CharField(null=False,max_length=20)
    mother_name=models.CharField(null=False,max_length=20)
    department_name=models.CharField(null=False,max_length=50,default='Chandigarh university')

class studentData(models.Model):
    uid=models.CharField(null=False,default='2139',max_length=20)
    subject=models.CharField(max_length=30)
    theory=models.IntegerField(max_length=10)
    practical=models.IntegerField(max_length=10)
    total=models.IntegerField(max_length=10)
    grade=models.CharField(max_length=10,default='NULL')

class topperData(models.Model):
    uid=models.CharField(null=False,default='2139',max_length=20)
    sum=models.IntegerField(max_length=10,default=0)

class signup(models.Model):
    names=models.CharField(default="myname",max_length=20)
    email=models.EmailField(default="ankit@gmail.com",max_length=20)
    username=models.CharField(default="ankit",max_length=20)
    password=models.CharField(default="my",max_length=20)

    

