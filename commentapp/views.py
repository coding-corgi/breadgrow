from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

# 댓글 생성 뷰
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    # 서버에서유저 생성
    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article =Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer =self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})


# 댓글 삭제뷰 /로그인여부확인
@method_decorator(comment_ownership_required, 'post')
@method_decorator(comment_ownership_required, 'get')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})