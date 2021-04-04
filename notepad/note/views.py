from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Note
from .serializers import NotesSerializer


class NotesView(APIView):
    """ Список записей """
    def get(self, request):
        notes = Note.objects.all()
        notes_serializer = NotesSerializer(notes, many=True)
        return Response(notes_serializer.data)
