from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """ Статьи блога """
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст')
    date_add = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Комментарии и оценки к статьям """
    RATINGS = (
        (0, 'Без оценки'),
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    message = models.TextField(default='', blank=True, verbose_name='Текст комментария')
    rating = models.IntegerField(default=0, choices=RATINGS, verbose_name='Оценка')

    def __str__(self):
        # https://django.fun/docs/django/ru/3.1/ref/models/instances/#django.db.models.Model.get_FOO_display
        return f'{self.get_rating_display()}: {self.message or "Без комментариев"}'
