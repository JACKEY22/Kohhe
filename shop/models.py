from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='shop')
    name = models.CharField(max_length=20, null=False, verbose_name='카페 이름')
    image = models.ImageField(upload_to='shop/', null=True, verbose_name='대표 사진')
    notice = models.CharField(max_length=50, verbose_name='공지')
    info = models.TextField(null=True, verbose_name='정보 or 소개글')
    address = models.CharField(max_length=50, null=True, verbose_name='주소')

    def __str__(self):
        return f'{self.name}'





