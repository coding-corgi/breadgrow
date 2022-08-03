from django.urls import path

from kcalculatorapp.views import KcalCreateView, KcalUpdateView, home, Kcl_detail, KcalDetailView, KcalGraphView

app_name ='kcalculatorapp'

# 첫번째는 내가 만들 주소 , 뷰 ,이름
urlpatterns = [
    path('home/', home, name='home'),
    path('create/', KcalCreateView.as_view(), name='create'),
    path('detail/<int:pk>', KcalDetailView.as_view(), name='detail'),
    path('graph/<int:pk>', KcalGraphView.as_view(), name='graph'),
    # path('detail/<int:pk>', Kcl_detail, name='kcldetail'),
    path('update/<int:pk>', KcalUpdateView.as_view(), name='update'),
]