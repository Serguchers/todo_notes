from rest_framework.viewsets import ModelViewSet

from .models import BaseUser
from .serializers import BaseUserSerializer


# Create your views here.
class UsersViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
