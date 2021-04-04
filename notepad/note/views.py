from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import NotesSerializer


class NotesView(APIView):
    """ Список записей """
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Получить токен текущего пользователя
        print('User token:', request.auth)

        notes = Note.objects.filter(author=request.user)
        notes_serializer = NotesSerializer(notes, many=True)
        return Response(notes_serializer.data)
