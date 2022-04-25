from django.urls import path
from .views import create_user, list_users

urlpatterns = [
    path('', list_users),
    path('add', create_user, name='create_user'),
]
