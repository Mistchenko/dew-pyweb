""" Настройка админки, документация: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/ """

from django.contrib import admin

from .models import Note

# Меняем формат вывода даты и времени только для РУССКОЙ локализации
# Для всего сайта надо поместить этот код в `settings.py`
from django.conf.locale.ru import formats as ru_formats
ru_formats.DATETIME_FORMAT = "d.m.Y H:i:s"


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Поля в списке
    list_display = ('title', 'public', 'date_add', 'author', 'id', )

    # Группировка поля в режиме редактирования
    fields = ('date_add', ('title', 'public'), 'message', 'author')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('date_add', )

    # Поиск по выбранным полям
    search_fields = ['title', 'message', ]

    # Фильтры справа
    list_filter = ('public', 'author', )

    def save_model(self, request, obj, form, change):
        # Добавляем текущего пользователя (если не выбран) при сохранении модели
        # docs: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
