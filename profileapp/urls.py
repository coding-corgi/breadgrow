from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

# 프로필 생성/수정 url
urlpatterns =[
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]