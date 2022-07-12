from django.urls import path

from kcalculatorapp.views import hello_world

app_name ='kcalculatorapp'

urlpatterns =[
    path('test/', hello_world, name='test'),
    # path('detail/<int:pk>', KcalDetailView, name='detail'),
]