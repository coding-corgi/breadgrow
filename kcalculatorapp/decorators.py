from django.http import HttpResponseForbidden

from kcalculatorapp.models import Kcal


def kcalculator_ownership_required(func):
    def decorated(request, *args, **kwargs):
        kcalculator = Kcal.objects.get(pk=kwargs['pk'])
        if not kcalculator.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated



