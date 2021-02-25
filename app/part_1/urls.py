from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import routers

from . import views

# Для ViewSet
router = DefaultRouter()
router.register(r'method3', views.Method3ViewSet, basename='method-3')

app_name = 'part_1'
urlpatterns = [
    path('method1/', views.Method1View.as_view(), name='method-1'),
    path('method2/', views.Method2View.as_view(), name='method-2'),
    path('method2/detail/<int:pk>/', views.Method2DetailView.as_view(), name='method-2-detail'),
    # Для ViewSet
    path('', include(router.urls))
]
