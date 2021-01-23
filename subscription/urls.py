from django.urls import path

from subscription.views import SubscriptionView

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]