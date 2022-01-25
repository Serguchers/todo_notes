from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo


class ProjectSerializer(serializers.ModelSerializer):
    related_users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'
        

class ToDoSerializer(serializers.ModelSerializer):
    related_project = serializers.StringRelatedField()
    owner = serializers.StringRelatedField() 
    class Meta:
        model = ToDo
        fields = '__all__'