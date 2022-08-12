from django.forms import ModelForm

from kcalculatorapp.models import Kcal

# 칼로리 계산기 커스텀 폼
class KcalCreationForm(ModelForm):
    class Meta:
        model = Kcal
        fields = ['height','weight','age','sex','actv','tension','goal','speed']