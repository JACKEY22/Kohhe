from django.contrib import admin

# Register your models here.
from subscription.models import Subscription

admin.site.register(Subscription)