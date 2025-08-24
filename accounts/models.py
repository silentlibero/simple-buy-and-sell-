from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    ROLE_CHOICES = [
        ('buyer', 'simple user'),
        ('costumer', 'want to sell'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, default='costumer')
    recent_buy = models.TextField(null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


