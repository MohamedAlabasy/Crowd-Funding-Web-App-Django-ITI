from django.urls import path
from user import views
from .views import user_profile, user_projects, user_donations, delete_user, update_user, verifyEmail,PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView


urlpatterns = [
     path('register', views.RegisterApiView.as_view(), name="register"),
     path('login', views.LoginApiView .as_view(), name="login"),
     path('email-verify', verifyEmail.as_view(), name="email-verify"),
     path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
     path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
     path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete'),    
     path('profile/<int:user_id>', user_profile),
     path('projects/<int:user_id>', user_projects),
     path('donations/<int:user_id>', user_donations),
     path('update', update_user),
     path('delete/<int:user_id>', delete_user),

]
# http://127.0.0.1:8000/user/password-reset/NQ/b5498v-b0a26759d93cb48ee0be866dadd12e77/?redirect_url=
