from django.db import models
from products.models import Product
from accounts.models import Profile
# Create your models here.


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
