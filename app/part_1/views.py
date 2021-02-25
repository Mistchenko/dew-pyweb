from django.shortcuts import render

from blog.models import Note


def home(request):
    context = {
        'message': 'Добро пожаловать',
        'left': 'Сообщение слева',
        'right': 'Сообщение справа',
    }
    return render(request, 'part_1/index.html', context)
