from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    """ Класс для аутентификации

    Пример:

    Authorization: Bearer 6ac75172d3f992fa9e2a98bb206c26a1b7ed54d3

    """
    keyword = 'Bearer'
