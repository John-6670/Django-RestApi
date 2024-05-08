from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .serializers import NoteSerializers
from .models import Note
from rest_framework.exceptions import PermissionDenied, ValidationError, NotFound
from django.db import models
from django.contrib.auth.models import User


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You need to be logged in to view notes.")
        
        return Note.objects.filter(models.Q(author=user) | models.Q(shared_with=user))
    
    def perform_create(self, serializer):
        user = self.request.user
        if not serializer.is_valid():
            raise ValidationError("Invalid data.")
        
        serializer.save(author=user)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(author=self.request.user)
        if not queryset.exists():
            raise NotFound("No notes found to delete.")
        
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You need to be logged in to view notes.")
        
        return Note.objects.filter(models.Q(author=user) | models.Q(shared_with=user))
    
    def update(self, request, *args, **kwargs):
        note = self.get_object()
        if note.author != request.user:
            raise PermissionDenied("You do not have permission to edit this note.")
        
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        note = self.get_object()
        if note.author != request.user:
            raise PermissionDenied("You do not have permission to edit this note.")
        
        return super().partial_update(request, *args, **kwargs)
