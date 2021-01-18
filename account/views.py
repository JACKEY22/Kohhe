from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from account.models import HelloWorld
# Create your views here.


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
