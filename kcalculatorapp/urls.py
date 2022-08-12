from django.urls import path

from kcalculatorapp.views import KcalCreateView, KcalUpdateView, home, KcalDetailView, KcalGraphView

app_name ='kcalculatorapp'

# 칼로리계산기  생성,상세페이지,수정,그래프/메인페이지 라우터
urlpatterns = [
    path('home/', home, name='home'),
    path('create/', KcalCreateView.as_view(), name='create'),
    path('detail/<int:pk>', KcalDetailView.as_view(), name='detail'),
    path('graph/<int:pk>', KcalGraphView.as_view(), name='graph'),
    path('update/<int:pk>', KcalUpdateView.as_view(), name='update'),
]