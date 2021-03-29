from rest_framework.serializers import ModelSerializer, Serializer, DecimalField, ListField, ChoiceField

from .models import Product


class ProductsSerializer(ModelSerializer):
    """ Сериализация списка товаров """
    price_sell = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'name', 'description', 'group', 'price', 'discount', 'price_sell', )


class QuerySerializer(Serializer):
    group = ListField(child=ChoiceField(choices=Product.GROUPS), required=False)
