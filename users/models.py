from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)     # nomi
    description = models.TextField()        #tavsifi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # narxi
    count = models.IntegerField(default=0)       # soni
    category_id = models.CharField(max_length=10, default=0)       #kategoriya identifikatori


class Warehouse(models.Model):
    name = models.CharField(max_length=100)      # nomi
    location = models.CharField(max_length=100)  # joylashuvi
    capacity = models.PositiveIntegerField()     # sig'imi
    manager = models.CharField(max_length=100)   # lavozimi


class Supplier(models.Model):
    phone_number = models.CharField(max_length=100, null=True)     # tel nomeri
    email = models.EmailField (max_length=100, default=1)        # emaili
    password = models.CharField (max_length=100, null= True)     # paroli
    address = models.CharField(max_length=100)      # manzili
