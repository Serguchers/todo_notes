from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'