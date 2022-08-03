from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView

from kcalculatorapp.decorators import kcalculator_ownership_required
from kcalculatorapp.forms import KcalCreationForm
from kcalculatorapp.models import Kcal




has_ownership = [kcalculator_ownership_required, login_required ]

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class KcalCreateView(CreateView):
    model = Kcal
    context_object_name = 'target_kcal'
    form_class = KcalCreationForm
    template_name = 'kcalculatorapp/create.html'



    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('kcalculatorapp:detail', kwargs={'pk':self.object.user.pk})







class KcalDetailView(DetailView):
    model = User
    context_object_name = 'target_kcal'
    template_name = 'kcalculatorapp/detail.html'


    def get_context_data(self, **kwargs):
        try:
            if self.request.user.kcal.sex == 'male':
                context = super().get_context_data(**kwargs)
                context['bmr'] = round((66 + (13.8 * self.request.user.kcal.weight + (5 * self.request.user.kcal.height)) - (6.8 * self.request.user.kcal.age)) * (self.request.user.kcal.actv))
                return context
            else:
                context = super().get_context_data(**kwargs)
                context['bmr'] = round((655 + (9.6 * self.request.user.kcal.weight + (1.8 * self.request.user.kcal.height)) - (4.7 * self.request.user.kcal.age)) * (self.request.user.kcal.actv))
                return context
        except:
             HttpResponseRedirect(reverse('kcalculatorapp:create'))


    # def get(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         try:
    #             if request.user.kcal.objects:
    #                 if request.user.kcal.sex == 'male':
    #                     bmr = round((1 * request.user.kcal.weight))
    #                     return bmr
    #                 else:
    #                     bmr = round((2 * request.user.kcal.weight))
    #                     return bmr
    #             return super().get(request,*args,**kwargs)
    #         except:
    #             return HttpResponseRedirect(reverse('kcalculatorapp:create'))
    #     else:
    #         return HttpResponseRedirect(reverse('kcalculatorapp:home'))
    #     return super().get(request,*args,**kwargs)


# def get_context_data(self, **kwargs):
#         try:
#             if self.request.user.kcal.sex == 'male':
#                 context = super().get_context_data(**kwargs)
#                 context['bmr'] = round((66 + (13.8 * self.request.user.kcal.weight + (5 * self.request.user.kcal.height)) - (
#                             6.8 * self.request.user.kcal.age)))
#                 return context
#             else:
#                 context = super().get_context_data(**kwargs)
#                 context['bmr'] = round((655 + (9.6 * self.request.user.kcal.weight + (1.8 * self.request.user.kcal.height)) - (
#                             4.7 * self.request.user.kcal.age)))
#                 return context
#         except:
#             return HttpResponseRedirect(reverse('kcalculatorapp:create'))
#





def Kcl_detail(request, pk):


    if request.method == 'GET':
        try:
            if request.user.kcal.objects:
                if request.user.kcal.sex == 'male':
                    bmr = round((1 * request.user.kcal.weight))
                    return  'kcalculatorapp/detail.html'
                else:
                    bmr = round((2 * request.user.kcal.weight))
                    return 'kcalculatorapp/detail.html'

        except:
            return HttpResponseRedirect(reverse('kcalculatorapp:create'))

    else:
        return HttpResponseRedirect(reverse('kcalculatorapp:home'))




    # def get(self, request, *args, **kwargs):
    #     try:
    #         return super().get(request)
    #     except:
    #         return reverse('kcalculatorapp:detail', kwargs={'pk': self.object.user.pk})



            # if self.request.user.kcal.sex == 'male':
            #     context = super().get_context_data(**kwargs)
            #     context['bmr'] = round((66 + ( 13.8 * self.request.user.kcal.weight + (5 * self.request.user.kcal.height)) - (6.8 * self.request.user.kcal.age)))
            #     return context
            # else:
            #     context = super().get_context_data(**kwargs)
            #     context['bmr'] = round((655 + (9.6 * self.request.user.kcal.weight + (1.8 * self.request.user.kcal.height)) - (4.7 * self.request.user.kcal.age)))
            #     return context


















        # reverse('kcalculatorapp:detail', kwargs={'pk': self.object.user.pk})














@method_decorator(kcalculator_ownership_required, 'get')
@method_decorator(kcalculator_ownership_required, 'post')
class KcalUpdateView(UpdateView):
    model = Kcal
    context_object_name = 'target_kcal'
    form_class = KcalCreationForm
    template_name = 'kcalculatorapp/update.html'

    def get_success_url(self):
        return reverse('kcalculatorapp:detail', kwargs={'pk':self.object.user.pk})



def home(request):
    return render(request, 'kcalculatorapp/home.html')


class KcalGraphView(DetailView):
    model = User
    context_object_name = 'target_kcal'
    template_name = 'kcalculatorapp/graph.html'