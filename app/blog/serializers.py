from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class AuthorSerializer(serializers.ModelSerializer):
    """ Автор статьи """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')


class NotesSerializer(serializers.ModelSerializer):
    """ Статьи для блога """

    # Меняем вывод, вместо `ID` пользователя будет `Имя`
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    # Этого поля нет в модели, это демонстрация, в данном случае не имеет практического применения
    ext_field = serializers.CharField(default='Внешний параметр')

    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'date_add', 'author', 'ext_field', ]


class NoteDetailSerializer(serializers.ModelSerializer):
    """ Одна статья блога """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        exclude = ('public', )  # Исключить эти поля

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        # date_add = datetime.strptime(ret['date_add'], '%Y-%m-%dT%H:%M:%S.%f') # Для даты с миллисекундами
        date_add = datetime.strptime(ret['date_add'], '%Y-%m-%dT%H:%M:%S')
        # Конвертируем дату в строку в новом формате
        ret['date_add'] = date_add.strftime('%d %B %Y %H:%M:%S')
        return ret


class NoteEditorSerializer(serializers.ModelSerializer):
    """ Добавление или изменение статьи """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['date_add', 'author', ]  # Только для чтения
