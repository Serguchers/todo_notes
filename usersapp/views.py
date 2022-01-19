from rest_framework import viewsets
from rest_framework import mixins

from .models import BaseUser
from .serializers import BaseUserSerializer


# Create your views here.
class UsersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    
