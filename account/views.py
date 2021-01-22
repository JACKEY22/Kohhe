from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.decorators import login_ownership_required
from account.models import HelloWorld
# Create your views here.
from account.forms import AccountUpdateFrom

permission = [login_required, login_ownership_required]

# after signing up, set log in status!!
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'account/detail.html'
    context_object_name = 'target_user'

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateFrom
    template_name = 'account/update.html'

    def get_success_url(self):
        return reverse_lazy('account:detail', kwargs={'pk':self.object.pk})

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(permission, 'get')
@method_decorator(permission, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')
    template_name = 'account/delete.html'


