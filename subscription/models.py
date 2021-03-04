from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from shop.models import Shop


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='subscription', null=True)
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_target', null=True)


