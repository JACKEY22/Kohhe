from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.forms import ShopCreateForm
from shop.models import Shop


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopCreateForm
    template_name = 'shop/create.html'

    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.owner = User.objects.get(pk=self.object.user.pk)
        temp_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home:home')


