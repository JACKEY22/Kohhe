from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from account.models import HelloWorld
# Create your views here.
from account.templates.account.forms import AccountUpdateFrom


def hello_world(request):

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

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'account/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"
    template_name = 'account/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateFrom
    success_url = reverse_lazy('account:hello_world')
    template_name = 'account/update.html'
