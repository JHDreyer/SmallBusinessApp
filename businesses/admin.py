from django.contrib import admin
from .models import Business, Product, Service

# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('businessname', 'businesstype', 'logo')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock_quantity', 'business')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'business')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)

