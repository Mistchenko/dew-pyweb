from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class Demo1(APIView):
    def get(self, request):
        return Response({'demo': 1})


class Demo2(APIView):
    def get(self, request):
        return Response({'demo': 2})


class Demo3(APIView):
    def get(self, request):
        return Response({'demo': 3})
