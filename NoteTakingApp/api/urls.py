from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='list-notes'),
    path('notes/<int:id>/', views.NoteRetrieveUpdateDestroy.as_view(), name='RUD-note'),
]
