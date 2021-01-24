from django.urls import path

from subscription.views import SubscriptionView, SubscriptionListView, SubscriptionFollowView

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('follow/', SubscriptionFollowView.as_view(), name='follow'),
    path('list/', SubscriptionListView.as_view(), name='list'),

]