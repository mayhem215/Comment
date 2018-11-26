from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=15, default=None)
    text = models.TextField("Текст комментария", max_length=500)
    vote = models.IntegerField(default=0)
