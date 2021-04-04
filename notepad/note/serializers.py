from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Note


class AuthorSerializer(serializers.ModelSerializer):
    """ Автор """
    class Meta:
        model = User
        fields = ('id', 'username', )


class NotesSerializer(serializers.ModelSerializer):
    """ Заметки в блокноте """

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'author', )
