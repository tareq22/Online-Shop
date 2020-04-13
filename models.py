from django.db import models

# Create your models here.

class Prolist(models.Model):
    serial = models.CharField(max_length=150)
    producttype = models.CharField(max_length=150)
    product = models.CharField(max_length=150)
    price = models.IntegerField()
    size = models.CharField(max_length=150)

    