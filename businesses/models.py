from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# dink ons moet dit opbreuk food .....
Business_Type = [
    ('restaurant', 'restaurant'),
    ('cosmetics', 'cosmetics'),
    ('clothing', 'clothing'),
    ('retail', 'retail'),
    ('freelance', 'freelance'),
    ('technology', 'technology'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    businessname = models.CharField(max_length=255)
    businesstype = models.CharField(max_length=255, choices=Business_Type)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, default='None')
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255, choices=Province)
    postal_code = models.CharField(max_length=255, default='None')
    logo = models.ImageField(default='None')

    def get_absolute_url(self):
        return reverse('businesses:blist')


class Product(models.Model):
    business = models.ForeignKey(
        'businesses.Business', related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.FloatField(max_length=10)
    stock_quantity = models.IntegerField()
    image = models.ImageField(default=None)

    # def get_absolute_url(self):
    # return reverse('businesses:plist')
