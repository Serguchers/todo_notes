from re import I
from django.db import models
from usersapp.models import BaseUser


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=128)
    repo_link = models.URLField(blank=True)
    related_users = models.ManyToManyField(BaseUser)
    
    def __str__(self) -> str:
        return self.project_name
    

class ToDo(models.Model):
    related_project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)