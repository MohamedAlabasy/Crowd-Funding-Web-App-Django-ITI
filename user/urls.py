from django.urls import path
from user import views
from .views import view_user_profile

urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name="register"),
    path('<int:user_id>', view_user_profile),
]
