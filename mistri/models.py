from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    is_mistri= models.BooleanField('is mistri',default=False)
    is_customer= models.BooleanField('is customer',default=False)

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    

class Mistriuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
