from rest_framework import serializers
from .models import Note


class NotesSerializer(serializers.ModelSerializer):
    """ Статьи для блога """
    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'date_add', ]


class NoteDetailSerializer(serializers.ModelSerializer):
    """ Одна статья блога """
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'date_add', 'public', 'author']


class NoteEditorSerializer(serializers.ModelSerializer):
    """ Добавление или изменение статьи """
    class Meta:
        model = Note
        # fields = "__all__"
        exclude = ('date_add', )  # Исключить это поле
