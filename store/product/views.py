from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, F, Min

from .models import Product
from .serializers import ProductsSerializer, QuerySerializer


class ProductsView(APIView):
    def get(self, request):
        products_model = Product.objects.filter(hide=False)

        # Отбор по группам
        query_params = QuerySerializer(data=request.query_params)
        if query_params.is_valid():
            if query_params.data.get('group'):
                q_group = Q()
                for grp in query_params.data['group']:
                    q_group |= Q(group=grp)
                products_model = products_model.filter(q_group)
        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        # Получаем минимальную скидку скидку
        min_price = products_model.aggregate(res=Min('price'))

        # Расчет цены продажи
        price_sell = F('price')*F('discount')
        products_model = products_model.annotate(price_sell=price_sell)

        products_serializer = ProductsSerializer(products_model, many=True)
        return Response({
            'min_price': min_price['res'],
            'products': products_serializer.data
        })
