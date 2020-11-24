from django.db import models

# Create your models here.
class Credentials(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=50)
    job_Class=models.IntegerField(default=1)
    regno=models.IntegerField(unique=True)

class School_Admin(models.Model):
   # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    Regno=models.IntegerField(unique=True)

class stand(models.Model):
    name=models.IntegerField()
class student(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    stand=models.IntegerField()
    tamil=models.IntegerField(default=0)
    science=models.IntegerField(default=0)
    Maths=models.IntegerField(default=0)
    Social=models.IntegerField(default=0)
    English=models.IntegerField(default=0)
    Regno=models.IntegerField(unique=True)

class staff(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    stand=models.IntegerField()
    Regno=models.IntegerField(unique=True)
    subj=models.CharField(max_length=25)







