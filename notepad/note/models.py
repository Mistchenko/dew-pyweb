from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """ Заметка в блокноте """
    title = models.CharField(max_length=160, verbose_name='Наименование блокнота')
    text = models.TextField(default='', blank=True, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title
