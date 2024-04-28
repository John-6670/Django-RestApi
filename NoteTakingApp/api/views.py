from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import NoteSerializers
from .models import Note
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(author=user)

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
