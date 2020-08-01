from django.contrib import admin
from .models import Business

# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('businessname', 'businesstype', 'logo')


admin.site.register(Business, BusinessAdmin)
