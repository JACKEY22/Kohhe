from django.urls import path

from shop.views import ShopCreateView, ShopListView, ShopDetailView

app_name = 'shop'

urlpatterns = [
    path('create/', ShopCreateView.as_view(), name='create'),
    path('list/', ShopListView.as_view(), name='list'),
    path('detail/<int:pk>', ShopDetailView.as_view(), name='detail'),


]