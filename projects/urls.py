from django.urls import path
from .views import create_project, create_comment, reply_comment, report_project, rate_project, cancel_project
#=======================================================================================#
#			                                URLS                                     	#
#=======================================================================================#

urlpatterns = [
    path('add', create_project),
    path('comment/add', create_comment),
    path('comment/reply/add', reply_comment),
    path('report/add', report_project),
    path('rate/<int:project_id>', rate_project),
    path('cancel/<int:project_id>', cancel_project),
    path('categories',),
]
