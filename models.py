from django.db import models


class Platforms(models.Model):
    businessname = models.CharField(max_length=255, default="Unknown")
    facebook = models.BooleanField(default=False)
    instagram = models.BooleanField(default=False)
    google = models.BooleanField(default=False)
    budget = models.CharField(max_length=200, default=None)
    extrainfo = models.CharField(max_length=300, default=None)
    budgetperiod = models.CharField(max_length=100, default=None)
