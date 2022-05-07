from django.urls import path

from .views import  FacebookSocialAuthView

urlpatterns = [
    path('facebook', FacebookSocialAuthView.as_view()),

]