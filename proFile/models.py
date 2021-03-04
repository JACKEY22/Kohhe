from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True, verbose_name='사진')
    nickname = models.CharField(max_length=20, unique=True, null=True, verbose_name='이름 또는 별명')
    message = models.CharField(max_length=100, null=True, verbose_name='상태 메세지')
    
