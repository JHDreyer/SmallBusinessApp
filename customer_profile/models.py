from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    user = models.ForeignKey(User, default =None, on_delete = models.CASCADE) 
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, default='None')
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, default='None')
    logo = models.ImageField(default='None')

class Product(models.Model):
    business = models.ForeignKey(Business, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.FloatField(max_length=10)
    image = models.ImageField(default=None)

class Contact(models.Model):
    user = models.ForeignKey(User, default =None, on_delete = models.PROTECT ) 
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)