from django.http import HttpResponse
from django.shortcuts import render
from account.models import HelloWorld
# Create your views here.


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        HelloWorld_obj = HelloWorld()
        HelloWorld_obj.text = temp
        HelloWorld_obj.save()

        return render(request, 'account/hello_world.html', context={'hello_world_output':HelloWorld_obj})

    else:
        return render(request, 'account/hello_world.html', context={'text':'GET METHOD!'})
