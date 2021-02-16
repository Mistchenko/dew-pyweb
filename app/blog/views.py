from rest_framework.response import Response
from rest_framework.views import APIView


class BlogListView(APIView):
    """ BlogListView """
    def get(self, request):
        return Response({})
