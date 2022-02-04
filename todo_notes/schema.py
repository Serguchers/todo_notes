import graphlib
import imp
import graphene
from graphene_django import DjangoObjectType
from todoapp.models import Project, ToDo
from usersapp.models import BaseUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class BaseUserType(DjangoObjectType):
    class Meta:
        model = BaseUser
        fields = '__all__'
        
class Query(graphene.ObjectType):
    all_todos = graphene.List(ToDoType)
    #all_projects = graphene.List(ProjectType)
    project_by_project_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_project_by_project_name(self, info, name=None):
        projects = Project.objects.all()
        if name:
            projects = projects.filter(project_name__exact=name)
        return projects
    
    def resolve_all_todos(root, info):
        return ToDo.objects.all()
    
    
schema = graphene.Schema(query=Query)