from rest_framework.response import Response
from rest_framework.views import APIView
from django.apps import apps


class BlogListView(APIView):
    """ BlogListView """
    def get(self, request):
        return Response({
            'verbose_name': apps.get_app_config('blog').verbose_name
        })
