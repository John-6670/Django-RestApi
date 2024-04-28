from rest_framework import generics
from .serializers import NoteSerializers
from .models import Note
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(author=user)


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        user = self.request.user
        return Note.objects.filter(author=user, id=id)
