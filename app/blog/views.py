from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note


class BlogListView(APIView):
    """ BlogListView """
    def get(self, request):
        notes = Note.objects.filter(public=True)

        res = []
        for note in notes:
            res.append({
                'id': note.id,
                'title': note.title,
                'author': {
                    'id': note.author.id,
                    'username': note.author.username,
                }
            })

        return Response(res)
