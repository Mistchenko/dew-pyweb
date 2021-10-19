from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, viewsets, permissions

from blog.models import Note
from part_1.models import Article
from part_1.serializers import ArticleSerializer


def home(request):
    """ Использование Django шаблонов.  Метод обрабатывает запрос `/` """

    # Объект который будет передан в шаблон
    context = {
        'title': 'Добро пожаловать',
        'left': 'генератор списка',
        'right': 'записи из базы данных',
        'data': [{'id': i, 'name': f'Name {i}'} for i in range(3)],
        'notes': Note.objects.all()
    }

    # Рендеринг шаблона с последующим ответом клиенту
    return render(request, 'part_1/index.html', context)


class Method1View(APIView):
    """ Работа с базовым классом APIView
    https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views
    """
    def get(self, request):
        """ Получить список всех записей """
        notes = Article.objects.all()
        notes_serializer = ArticleSerializer(notes, many=True)
        return Response(notes_serializer.data)

    def post(self, request):
        """ Добавить новую статью """
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Method2View(generics.ListCreateAPIView):
    """ реализация с помощью Generic views и mixin
    https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class Method2DetailView(generics.RetrieveUpdateDestroyAPIView):
    """ CRUD для записи
    Все возможные миксины
    https://www.django-rest-framework.org/api-guide/generic-views/#mixins
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class Method3ViewSet(viewsets.ModelViewSet):
    """ реализация с помощью ViewSet
    https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
