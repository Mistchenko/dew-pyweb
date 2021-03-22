from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from .models import Note
from .serializers import NotesSerializer, NoteDetailSerializer, NoteEditorSerializer


class NotesView(APIView):
    """ Статьи для блога """

    def get(self, request):
        """ Получить статьи для блога """
        notes = Note.objects.filter(public=True).order_by('-date_add', 'title')
        serializer = NotesSerializer(notes, many=True)

        return Response(serializer.data)


class NoteDetailView(APIView):
    """ Статя блога """

    def get(self, request, note_id):
        """ Получить статю """
        note = Note.objects.filter(pk=note_id, public=True).first()

        if not note:
            raise NotFound(f'Опубликованная статья с id={note_id} не найдена')

        serializer = NoteDetailSerializer(note)
        return Response(serializer.data)


class NoteEditorView(APIView):
    """ Добавление или изменение статьи """
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        """ Новая статья для блога """

        new_note = NoteEditorSerializer(
            data={
                **request.data,
                'author': request.user.pk
            }
        )

        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)
