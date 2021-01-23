from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop')
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='shop/', null=True)

    notice = models.CharField(max_length=50)
    info = models.TextField(null=True)

    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'





