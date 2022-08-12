from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# 계정 인증확인 데코레이터
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated


