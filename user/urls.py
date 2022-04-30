from django.urls import path
from user import views
from .views import user_profile, user_projects, user_donations

urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name="register"),

    path('profile/<int:user_id>', user_profile),
    path('projects/<int:user_id>', user_projects),
    path('donations/<int:user_id>', user_donations),
]
