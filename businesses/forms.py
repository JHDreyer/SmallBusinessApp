from django import forms
from .models import Business, Product, Service


class BusinessForm(forms.ModelForm):
    CHOICES = ()

    class Meta:
        model = Business
        fields = ('businessname', 'businesstype', 'city',
                  'address', 'address2', 'postal_code', 'logo')

        labels = {
            "name": "eg Village Shop",
            "type": "Choose...",
            "province": "Choose...",
            "address": "eg 1234 Main St",
            "address2": "eg Apartment, studio, or floor"
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
