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
    (0.45, '저강도'),
    (0.55, '중강도'),
    (0.65, '고강도'),
)

DIET_LEAN =(
    ('diet', '다이어트-체지방감소'),
    ('lean', '린매스-근육증가'),
)

SPEED =(
    (300, '천천히'),
    (500, '빠르게'),
)




class Kcal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kcal', null=True)
    height = models.PositiveIntegerField(default='',  null=False , verbose_name='키', )
    weight = models.FloatField(default='',  null=False, verbose_name='체중')
    age = models.PositiveIntegerField(default='',  null=False, verbose_name='나이')
    sex = models.CharField(max_length=200, choices=SEX_CHOICE,  null=False, verbose_name='성별')
    actv = models.FloatField(max_length=200, choices=ACTV_CHOICE, null=False, verbose_name='활동량')
    tension =models.FloatField(max_length=200, choices=TENSION_CHOICE,  null=False, verbose_name='운동강도')
    created_at = models.DateField(auto_now_add=True, null=True)
    goal = models.CharField(max_length=200, choices=DIET_LEAN,  null=False, verbose_name='운동목적')
    speed = models.PositiveIntegerField(max_length=200, choices=SPEED, null=False, verbose_name='체중변화 속도')








#
#
#
# class Kcal(models.Model):
#     height = models.PositiveIntegerField(default='',  null=False , verbose_name='height')
#     weight = models.PositiveIntegerField(default='',  null=False, verbose_name='weight')
#     age = models.PositiveIntegerField(default='',  null=False, verbose_name='age')
#     sex = models.CharField(max_length=200, choices=SEX_CHOICE,  null=False, verbose_name='sex')
#
#
#

