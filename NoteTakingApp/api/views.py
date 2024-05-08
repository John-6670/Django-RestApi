from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import NoteSerializers
from .models import Note
from rest_framework.exceptions import PermissionDenied, ValidationError, NotFound


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You need to be logged in to view notes.")
        
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if not serializer.is_valid():
            raise ValidationError("Invalid data.")
        
        serializer.save(author=user)

    def delete(self):
        queryset = self.get_queryset()
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
        
        return Note.objects.filter(author=user)
