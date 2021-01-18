from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.models import HelloWorld
# Create your views here.
from account.forms import AccountUpdateFrom


def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            temp = request.POST.get('hello_world_input')

            hello_world = HelloWorld()
            hello_world.text = temp
            hello_world.save()

            hello_world_list = HelloWorld.objects.all()

            # return HttpResponseRedirect(reverse('account:hello_world'))
            return redirect('account:hello_world')

        else:
            hello_world_list = HelloWorld.objects.all()

            return render(request, 'account/hello_world.html', context={'hello_world_list':hello_world_list})
    else:
        return redirect('account:login')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'account/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'account/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateFrom
    success_url = reverse_lazy('account:hello_world')
    template_name = 'account/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')
    template_name = 'account/delete.html'

