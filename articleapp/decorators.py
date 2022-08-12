
from django.http import HttpResponseForbidden

from articleapp.models import Article

# 계정 인증확인 데코레이터
def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

