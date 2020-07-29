from django.contrib import admin
from .models import Business, Contact

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'logo')


class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'subject')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Contact, ContactAdmin)
