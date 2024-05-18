from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'author', 'title', 'body', 'created', 'updated', 'shared_with']
