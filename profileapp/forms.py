from django.forms import ModelForm

from profileapp.models import Profile

# 프로필 생성 커스텀 폼
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

