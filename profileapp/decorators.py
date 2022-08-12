
from django.http import HttpResponseForbidden

from profileapp.models import Profile

# # 계정 인증확인 데코레이터
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated


