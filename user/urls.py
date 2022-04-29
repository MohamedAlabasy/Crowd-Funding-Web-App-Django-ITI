from django.urls import path
from user import views

urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name="register")
]