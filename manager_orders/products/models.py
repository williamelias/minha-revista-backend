from django.db import models
from authentication.models import Customer
# Create your models here.

class Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.FileField(upload_to=None, max_length=100)

