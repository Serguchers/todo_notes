from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo
from usersapp.serializers import BaseUserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    related_users = BaseUserSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
        

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'