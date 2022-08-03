from django.contrib.auth.models import User
from django.db import models

# Create your models here.
SEX_CHOICE =(
    ('male', '남자'),
    ('female', '여자'),
)

ACTV_CHOICE =(
    (1.2, '주1-2회 운동 | 좌식 생활'),
    (1.375, '주2-3회 운동 | 적은 활동'),
    (1.55, '주3-4회 운동 | 평균적 활동'),
    (1.6375, '주4-5회 운동 | 평균 ~ 많은 활동'),
    (1.725, '주5-6회 운동 | 많은 활동'),
    (1.9, '주7회 하루 2번운동 | 아주 많은활동'),
)

TENSION_CHOICE =(
    ('low', '저강도'),
    ('mid', '중강도'),
    ('high', '고강도'),
)





class Kcal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kcal', null=True)
    height = models.PositiveIntegerField(default='',  null=False , verbose_name='키')
    weight = models.PositiveIntegerField(default='',  null=False, verbose_name='체중')
    age = models.PositiveIntegerField(default='',  null=False, verbose_name='나이')
    sex = models.CharField(max_length=200, choices=SEX_CHOICE,  null=False, verbose_name='성별')
    actv = models.FloatField(max_length=200, choices=ACTV_CHOICE, null=False, verbose_name='활동량')
    tension =models.CharField(max_length=200, choices=TENSION_CHOICE,  null=False, verbose_name='운동강도')
    created_at = models.DateField(auto_now_add=True, null=True)
