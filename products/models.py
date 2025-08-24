from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=250, blank=True, null=True)
    creat_at = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
