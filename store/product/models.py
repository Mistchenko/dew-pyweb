from django.db import models


class Product(models.Model):
    """ Товары """
    GROUPS = (
        (0, 'Прочее'),
        (1, 'Выпечка'),
        (2, 'Молочные продукты'),
        (3, 'Мясные продукты'),
    )
    name = models.CharField(max_length=160, verbose_name='Наименование продукта')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    hide = models.BooleanField(default=False, blank=True, verbose_name='Продукт скрыт')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Цена')
    discount = models.DecimalField(max_digits=6, decimal_places=4, default=0, blank=True, verbose_name='Коэффициент')
    group = models.IntegerField(default=0, blank=True, verbose_name='Группа товара')
