from rest_framework import serializers
from blog.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'public', ]
