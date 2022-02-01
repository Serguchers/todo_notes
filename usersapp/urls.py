from django.urls import path
from .views import UsersViewSet


app_name = 'usersapp'
urlpatterns = [
    path('', UsersViewSet.as_view({'get': 'list'}))
]
