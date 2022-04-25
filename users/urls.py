from django.urls import path
from .views import create_user

urlpatterns = [
    path('', create_user, name='create_user')
]
