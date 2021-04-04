# Написание пользовательских команд для django-admin
# https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Генератор токенов для всех пользователей'

    def add_arguments(self, parser):
        parser.add_argument('del', nargs='?', help='Сначала удалить существующие')

    def handle(self, *args, **options):
        print(self.help)
        if options['del']:
            # Удаляем существующие токены если передан праметр --del
            self.del_tokens()
        self.get_or_create()

    @staticmethod
    def get_or_create():
        """ Создать токен если нет """
        for user in User.objects.all():
            token, created = Token.objects.get_or_create(user=user)
            print(user.username, token.key, 'created:', created)

    @staticmethod
    def del_tokens():
        """ Создать новый токен можно только удалив старый"""
        delete = Token.objects.all().delete()
        print('Удалено:', delete[0])
        # self.get_or_create()
