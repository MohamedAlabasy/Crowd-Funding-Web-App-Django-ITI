from django.urls import path
from user import views
from .views import user_profile, user_projects, user_donations, delete_user, update_user, verifyEmail


urlpatterns = [
    path('register', views.RegisterApiView.as_view(), name="register"),
    path('login', views.LoginApiView .as_view(), name="login"), 
    path('email-verify', verifyEmail.as_view(), name="email-verify"),
    path('profile/<int:user_id>', user_profile),
    path('projects/<int:user_id>', user_projects),
    path('donations/<int:user_id>', user_donations),
    path('update', update_user),
    path('delete/<int:user_id>', delete_user),

]
