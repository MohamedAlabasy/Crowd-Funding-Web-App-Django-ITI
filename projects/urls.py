from django.urls import path
from .views import create_project, create_comment
#=======================================================================================#
#			                                URLS                                     	#
#=======================================================================================#

urlpatterns = [
    path('add', create_project),
    path('comment/add', create_comment),
]
