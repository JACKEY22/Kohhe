from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView

from shop.forms import ShopCreateForm
from shop.models import Shop

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopCreateForm
    template_name = 'shop/create.html'

    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.owner = self.request.user
        temp_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shop:detail', kwargs={'pk':self.object.pk })

class ShopListView(ListView):
    model = Shop
    template_name = 'shop/list.html'
    context_object_name = 'shop_list'
    paginate_by = 10

class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop/detail.html'
    # form_class = ShopCreateForm
    context_object_name = 'target_shop'






