from django.urls import path

from .views import ProductsView


app_name = 'product'

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
]
