from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = django가 자동으로 주가해주는 칼럼

    # 유저 모델을 참조하는 경우
    # # 방법1(권장 x)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # # 방법2(권장 o), settings.AUTH_USER_MODEL == 'account.User'
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법3(권장 o)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id = 

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = django가 자동으로 추가해주는 칼럼

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id =