from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from shop.models import Shop
from subscription.models import Subscription


@method_decorator(login_required(login_url='account:login'), 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:detail', kwargs={'pk':self.request.GET.get('shop_pk')})

    def get(self, request, *args, **kwargs):

        shop = get_object_or_404(Shop, pk=self.request.GET.get('shop_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, shop=shop)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, shop=shop).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)