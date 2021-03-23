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

        # Передаем в сериалайзер (валидатор) данные из запроса
        new_note = NoteEditorSerializer(data=request.data)

        # Проверка параметров
        if new_note.is_valid():
            # Записываем новую статью и добавляем текущего пользователя как автора
            new_note.save(author=request.user)
            return Response(new_note.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, note_id):

        # Находим редактируемую статью
        note = Note.objects.filter(pk=note_id, author=request.user).first()
        if not note:
            raise NotFound(f'Статья с id={note_id} для пользователя {request.user.username} не найдена')

        # Для сохранения изменений необходимо передать 3 параметра
        # Объект связанный со статьей в базе: `note`
        # Изменяемые данные: `data`
        # Флаг частичного оновления (т.е. можно проигнорировать обязательные поля): `partial`
        new_note = NoteEditorSerializer(note, data=request.data, partial=True)

        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, status=status.HTTP_200_OK)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)
