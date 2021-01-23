from django.urls import path

from subscription.views import SubscriptionView, SubscriptionListView

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]