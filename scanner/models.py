from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Product(models.Model):
    code = models.CharField(max_length=50,default="")
    origin= models.CharField(max_length=50)
    type= models.CharField(max_length=50)
    harvest_date= models.DateField()
    pkg_date = models.DateField()
    distributor = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    store=models.CharField(max_length=50)
    certifications =models.CharField(max_length=50)


