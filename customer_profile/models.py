from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# dink ons moet dit opbreuk food .....
Business_Type = [
    ('Service Provider', 'Service Provider'),
    ('Commerce', 'Commerce')
]
Province = [
    ('Eastern Cape', 'Eastern Cape'),
    ('Free State', 'Free State'),
    ('Gauteng', 'Gauteng'),
    ('KwaZulu-Natal', 'KwaZulu-Natal'),
    ('Limpopo', 'Limpopo'),
    ('Mpumalanga', 'Mpumalanga'),
    ('Northern Cape', 'Northern Cape'),
    ('North West', 'North West'),
    ('Western Cape', 'Western Cape')
]
# Create your models here.


class Business(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=Business_Type)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, default='None')
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255, choices=Province)
    postal_code = models.CharField(max_length=255, default='None')
    logo = models.ImageField(default='None')

    def get_absolute_url(self):
        return reverse('customer_profile:list')


class Product(models.Model):
    business = models.ForeignKey(
        Business, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.FloatField(max_length=10)
    image = models.ImageField(default=None)


class Contact(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
