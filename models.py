from django.db import models

class prolist(models.Model):
    serial=models.CharField(max_length=10)
    prodcuttype=models.CharField(max_length=10)
    product=models.CharField(max_length=10)
    price=models.IntegerField()
    size=models.CharField(max_length=10)



