from django.test import TestCase, Client
from api.models import Note

class NoteApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def tes_list_notes(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        data = {
            'author': 1, 
            'title': 'Test Note',
            'body': 'This is a test note.'
        }
        response = self.client.post('/api/notes/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Note.objects.count(), 1)
    
    