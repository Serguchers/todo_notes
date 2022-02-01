from rest_framework import viewsets
from rest_framework import mixins

from .models import BaseUser
from .serializers import BaseUserSerializer, BaseUserSerializerExtended


# Create your views here.
class UsersViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    
    def get_serializer_class(self):
        if self.request.version == '2':
            return BaseUserSerializerExtended
        return BaseUserSerializer
    
