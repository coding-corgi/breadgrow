from django.forms import ModelForm

from commentapp.models import Comment

# 댓글 커스텀 폼
class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields =['content']