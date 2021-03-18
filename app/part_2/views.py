import json

from django.db.models import Q, F
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from blog import models
from .serializers import note_serializer


class DjView(View):
    def get(self, request):
        if request.body:
            note = json.loads(request.body)
            # Документация https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#get-object-or-404
            note_model = get_object_or_404(models.Note, pk=note['note_id'])
            notes = [note_serializer(note_model), ]
        else:
            note_model = models.Note.objects.filter(title='title')
            note_model = note_model.order_by('-date_add', 'title')
            # Это НЕ срез, это переопределенная реализация [ OFFSET : LIMIT ]
            # note_model = note_model[0:3]
            notes = [note_serializer(note) for note in note_model]

        return JsonResponse({"notes": notes})
        # Избежать ошибки TypeError
        # return JsonResponse([1, 2, 3], safe=False)

    def post(self, request):
        # Отключен csrf
        # Добавление новой записи
        note = json.loads(request.body)

        author = User.objects.get(id=note['author_id'])

        note_model = models.Note(
            title=note['title'],
            message=note.get('message', ''),
            public=note.get('public', False),
            author=author
        )

        note_model['public']=False

        # Сохранение отдельной строкой
        note_model.save()

        return JsonResponse({'note': note_serializer(note_model)})

    def patch(self, request):
        # Изменение существующей записи
        note = json.loads(request.body)
        note_model = models.Note.objects.get(pk=note['id'])
        if note.get('title'):
            note_model.title = note.get('title')
        if note.get('message'):
            note_model.message = note.get('message')

        note_model.public = note.get('public', False)

        note_model.save()
        return JsonResponse({'note': note_serializer(note_model)})

    def delete(self, request):
        # Удаление записи
        note_id = request.GET.get('note_id')
        if note_id:
            note_model = models.Note.objects.filter(id=note_id).delete()
            return JsonResponse({'delete': note_model})
        else:
            return JsonResponse({'note_id': "Обязательный параметр"})
