from rest_framework.serializers import HyperlinkedModelSerializer
from .models import BaseUser


class BaseUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']