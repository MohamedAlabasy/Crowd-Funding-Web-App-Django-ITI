from django.urls import path
from user import views
from .views import view_user_profile, view_user_projects

urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name="register"),

    path('profile/<int:user_id>', view_user_profile),
    path('projects/<int:user_id>', view_user_projects),
]
