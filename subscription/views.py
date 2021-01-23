from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from article.models import Article
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


class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscription/list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            shops = Subscription.objects.filter(user=self.request.user).values_list('shop')
            article_list = Article.objects.filter(shop__in=shops)
        else:
            article_list = Article.objects.all()
        return article_list
