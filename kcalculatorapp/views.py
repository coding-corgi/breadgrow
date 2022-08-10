from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView

from kcalculatorapp.decorators import kcalculator_ownership_required
from kcalculatorapp.forms import KcalCreationForm
from kcalculatorapp.models import Kcal

has_ownership = [kcalculator_ownership_required, login_required]


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
        return reverse('kcalculatorapp:detail', kwargs={'pk': self.object.user.pk})


class KcalDetailView(DetailView):
    model = User
    context_object_name = 'target_kcal'
    template_name = 'kcalculatorapp/detail.html'



    def dispatch(self, request, *args, **kwargs):
        try:
            if not self.request.user:
                return HttpResponseRedirect(reverse('kcalculatorapp:create'))
            return super(KcalDetailView, self).dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('kcalculatorapp:create'))







    def get_context_data(self, **kwargs):

        kcl = self.request.user.kcal
        men_kcal = round((66 + (13.8 * kcl.weight + (5 * kcl.height)) - (6.8 * kcl.age)) * (kcl.actv))
        women_kcal = round((655 + (9.6 * kcl.weight + (1.8 * kcl.height)) - (4.7 * kcl.age)) * (kcl.actv))
        context = super().get_context_data(**kwargs)

        if kcl.sex == 'male':
            if kcl.goal == 'diet':
                context['bmr'] = men_kcal - 500

            else:
                context['bmr'] = men_kcal + 500

        else:
            if kcl.goal == 'diet':
                context['bmr'] = women_kcal - 500

            else:
                context['bmr'] = women_kcal + 500
        bmr = context['bmr']

        carbo_per = round(kcl.tension * 100)
        carbo_kcal = round(bmr * kcl.tension)

        carbo_g = round(carbo_kcal / 4)
        proten_g = round(kcl.weight * 1.6)

        proten_kcal = proten_g * 4
        fat_kcal = bmr - carbo_kcal - proten_kcal
        fat_g = round(fat_kcal / 9)

        proten_per = round((proten_kcal / bmr) * 100)
        fat_per = 100 - carbo_per - proten_per
        context['kcl'] = {'carbo_per': carbo_per, 'proten_per': proten_per, 'fat_per': fat_per, 'carbo_kcal': carbo_kcal, 'proten_kcal': proten_kcal, 'fat_kcal': fat_kcal, 'carbo_g': carbo_g, 'proten_g': proten_g,
                          'fat_g': fat_g}
        return context




    #
    # if request.user.is_anonymous:
    #     user_membership = None
    # else:
    #     try:
    #         user_membership = Customer.objects.get(user=self.request.user)
    #     except Customer.DoesNotExist:
    #         user_membership = None
    # kwargs['user_membership'] = user_membership
    # return super().get_context_data(**kwargs)


@method_decorator(kcalculator_ownership_required, 'get')
@method_decorator(kcalculator_ownership_required, 'post')
class KcalUpdateView(UpdateView):
    model = Kcal
    context_object_name = 'target_kcal'
    form_class = KcalCreationForm
    template_name = 'kcalculatorapp/update.html'

    def get_success_url(self):
        return reverse('kcalculatorapp:detail', kwargs={'pk': self.object.user.pk})


def home(request):
    return render(request, 'kcalculatorapp/home.html')


class KcalGraphView(DetailView):
    model = User
    context_object_name = 'target_kcal'
    template_name = 'kcalculatorapp/graph.html'
