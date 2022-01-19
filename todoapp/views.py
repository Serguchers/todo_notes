from django.shortcuts import get_object_or_404
from django.template import context
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer
from .filters import ProjectFilter


# Create your views here.
class ProjectPagination(LimitOffsetPagination):
    default_limit = 10
    
class ToDoPagination(LimitOffsetPagination):
    default_limit = 20
    
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    filterset_class = ProjectFilter

class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoPagination
    
    def destroy(self, request, pk=None):
        note = get_object_or_404(ToDo, pk=pk)
        note.is_active = False
        note.save()
        serializer_context = {
            'request': request,
        }
        serializer = ToDoSerializer(note, context=serializer_context)
        return Response(serializer.data)