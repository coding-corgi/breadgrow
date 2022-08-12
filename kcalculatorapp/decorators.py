from django.http import HttpResponseForbidden

from kcalculatorapp.models import Kcal

# 계정 인증확인 데코레이터#
def kcalculator_ownership_required(func):
    def decorated(request, *args, **kwargs):
        kcalculator = Kcal.objects.get(pk=kwargs['pk'])
        if not kcalculator.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated



