from django.contrib.auth.models import User
from django.db import models


# 게시글 커스텀 모델 /
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now=True, null=True)

    # 날짜 역순 게시
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title

