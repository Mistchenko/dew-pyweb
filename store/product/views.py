from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, F, Min, Max

from .models import Product
from .serializers import ProductsSerializer, QuerySerializer


class ProductsView(APIView):
    def get(self, request):
        products_model = Product.objects.filter(hide=False)

        # Отбор по группам
        query_params = QuerySerializer(data=request.query_params)
        if query_params.is_valid():
            if query_params.data.get('group'):
                products_model = products_model.filter(group__in=query_params.data['group'])
        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        # Пример с ИЛИ
        # p1 = Q(group=2)
        # p2 = Q(discount=0)
        # products_model = products_model.filter(p1 | p2)

        # Получаем минимальную и максимальную цены
        prices = products_model.aggregate(min_price=Min('price'), max_price=Max('price'))

        # Расчет цены продажи
        price_sell = F('price')*F('discount')
        products_model = products_model.annotate(price_sell=price_sell)

        products_serializer = ProductsSerializer(products_model, many=True)
        return Response({
            'min_price': prices['min_price'],
            'max_price': prices['max_price'],
            'products': products_serializer.data
        })
