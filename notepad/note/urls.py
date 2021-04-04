from django.urls import path

from .views import NotesView


app_name = 'note'

urlpatterns = [
    path('notes/', NotesView.as_view(), name='notes'),
]
