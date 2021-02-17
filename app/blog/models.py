from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title
