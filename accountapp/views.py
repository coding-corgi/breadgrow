from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HellWorld


def hello_world(request):
    if  request.method == 'POST':

        temp = request.POST.get('hello_input')

        new_hello= HellWorld()
        new_hello.text = temp
        new_hello.save()

        return HttpResponseRedirect(reverse('accountapp:test'))

    else:
        list = HellWorld.objects.all()

        return render(request, 'accountapp/helloworld.html', context={'hello_list': list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:test')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
