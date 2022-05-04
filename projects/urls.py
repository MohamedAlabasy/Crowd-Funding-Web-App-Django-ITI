from django.urls import path
from .views import all_project, add_project_images, project_pictures, get_all_tags, donate_project, get_latest_projects, show_project, show_similar_project, create_project, create_comment, reply_comment, report_project, rate_project, cancel_project, all_categories

#=======================================================================================#
#			                                URLS                                     	#
#=======================================================================================#

urlpatterns = [
    path('', all_project),
    path('add', create_project),
    path('comment/add', create_comment),
    path('comment/reply/add', reply_comment),
    path('report/add', report_project),
    path('cancel/<int:project_id>', cancel_project),
    path('show/<int:project_id>', show_similar_project),
    path('single/<int:project_id>', show_project),
    path('latest', get_latest_projects),
    path('categories', all_categories),
    path('tags', get_all_tags),
    path('rate/<int:project_id>', rate_project),
    path('donate/<int:project_id>', donate_project),
    path('pictures/<int:project_id>', project_pictures),
    path('add/images', add_project_images),

]
