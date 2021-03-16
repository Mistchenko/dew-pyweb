from django.urls import path, include
from . import views

app_name = 'part-2'
urlpatterns = [
    path('dj/', views.DjView.as_view(), name='dj'),
]
