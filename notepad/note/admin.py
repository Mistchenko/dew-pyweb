from django.contrib import admin
from .models import Note
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', )
