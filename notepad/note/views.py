from rest_framework.views import APIView
from rest_framework.response import Response


class NotesView(APIView):
    """ Список записей """
    def get(self, request):
        return Response([])
