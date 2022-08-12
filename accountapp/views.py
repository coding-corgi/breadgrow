from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from django.urls import  reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, CustomUserCreationForm

# 로그인 여부/ 계정주인 확인 데코레이터 묶음
has_ownership = [account_ownership_required, login_required]

# 계정 생성 뷰
class AccountCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('kcalculatorapp:home')
    template_name = 'accountapp/create.html'

# 계정 상세페이지 뷰
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


# 계정 수정 뷰 / 계정인증확인
@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:test')
    template_name = 'accountapp/update.html'

# 계정 삭제 뷰
@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'



