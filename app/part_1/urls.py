from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'mix/', views.BlogViewMix)

app_name = 'demo'
urlpatterns = [
    path('v1/', views.Demo1.as_view(), name='demo-1'),
    path('v2/', views.Demo2.as_view(), name='demo-2'),
    path('v3/', views.Demo3.as_view(), name='demo-3'),
    # path('', include(router.urls))
]
