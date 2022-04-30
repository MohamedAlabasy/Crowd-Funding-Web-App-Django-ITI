from django.urls import path
from .views import create_project, create_comment, reply_comment
#=======================================================================================#
#			                                URLS                                     	#
#=======================================================================================#

urlpatterns = [
    path('add', create_project),
    path('comment/add', create_comment),
    path('comment/reply/add', reply_comment),
]
