from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from shop.models import Shop


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True, verbose_name='제목')
    content = models.TextField(null=True, verbose_name='내용')
    image = models.ImageField(upload_to='article/', null=False, verbose_name='사진')
    created_at = models.DateField(auto_created=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, related_name='article', null=True, blank=True, verbose_name='카페')

