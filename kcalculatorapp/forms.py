from django.forms import ModelForm

from kcalculatorapp.models import Kcal


class KcalCreationForm(ModelForm):
    class Meta:
        model = Kcal
        fields = ['height','weight','age','sex','actv','tension','goal','speed']