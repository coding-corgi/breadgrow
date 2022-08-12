from django import forms
from django.forms import ModelForm

from articleapp.models import Article

# 게시글 커스텀 폼
class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable text-start',
                                                           'style':'height:auto;'}))
    class Meta:
        model = Article
        fields = ['title','image','content']