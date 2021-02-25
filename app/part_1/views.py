from django.shortcuts import render

from blog.models import Note


def home(request):
    """ Использование Django шаблонов.  Метод обрабатывает запрос `/` """

    # Объект который будет передан в шаблон
    context = {
        'message': 'Добро пожаловать',
        'left': 'сообщение слева',
        'right': 'сообщение справа',
    }

    # Рендеринг шаблона с последующим ответом клиенту
    return render(request, 'part_1/index.html', context)


