from django.urls import path
from .views import (
    ViewUsers,
    CreateUser
)


urlpatterns = [
    path('', ViewUsers.as_view(), name='users'),
    path('create/', CreateUser.as_view(), name='create')

]