import json
from urllib import request, response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from usersapp.models import BaseUser as User
from .views import ProjectViewSet
from .models import Project, ToDo
from uuid import uuid4

class TestProjectViewSet(TestCase):
    factory = APIRequestFactory()
    
    def test_get_list(self):
        request = self.factory.get('/api/projects/')
        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin123456', uuid=uuid4())
        force_authenticate(request, admin)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_project(self):
        project = mixer.blend(Project)
        request = self.factory.post('/api/projects/', {'project_name': project.project_name,
                                                       'repo_link': '', 'related_users': project.related_users})
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_ToDo_get_detail(self):
        client = APIClient()
        admin = User.objects.create_superuser('admin2', 'admin@admin.com', 'admin123456', uuid=uuid4())
        note = mixer.blend(ToDo)
        client.force_authenticate(admin)
        response = client.get(f'/api/todos/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()
    
    def test_ToDo_unauthorized_update(self):
        client = APIClient()
        note = mixer.blend(ToDo, owner__uuid=uuid4())
        response = client.put(f'/api/todos/{note.id}/', {'text': 'random text'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestToDosViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_note(self):
        admin = User.objects.create_superuser('admin3', 'admin@admin.com', 'admin123456', uuid=uuid4())
        note = mixer.blend(ToDo, owner__uuid=uuid4())
        self.client.force_login(admin)
        response = self.client.get(f'/api/todos/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)