from django.contrib import admin
from . models import Platforms
# Register your models here.

class PlatfromAdmin(admin.ModelAdmin):
     list_display = ('facebook', 'instagram','google', 'budget', 'budgetperiod')

admin.site.register(Platforms, PlatfromAdmin)