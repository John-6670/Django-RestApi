from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class NoteSerializers(serializers.ModelSerializer):
    shared_with = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=User.objects.all(),  # this will be overridden by the view
        required=False
    )
    
    class Meta:
        model = Note
        fields = ['id', 'author', 'title', 'body', 'created', 'updated', 'shared_with']
