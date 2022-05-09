from django.urls import path
from .views import all_comments, latest_admin_selected, report_comment, highest_rate, search_bar_tag, search_bar_title, project_category, all_project, add_project_images, get_all_tags, donate_project, get_latest_projects, show_project, create_project, create_comment, reply_comment, report_project, rate_project, cancel_project, all_categories
# project_pictures ,
#=======================================================================================#
#			                                URLS                                     	#
#=======================================================================================#

urlpatterns = [
    path('', all_project),
    path('add', create_project),
    path('comment/add', create_comment),
    path('comment/reply/add', reply_comment),
    path('comment/report', report_comment),
    path('report', report_project),
    path('cancel/<int:project_id>', cancel_project),
    path('single/<int:project_id>', show_project),
    path('latest', get_latest_projects),
    path('categories', all_categories),
    path('tags', get_all_tags),
    path('rate', rate_project),
    path('donate', donate_project),
    # path('pictures/<int:project_id>', project_pictures),
    path('add/images', add_project_images),
    path('category/<int:category_id>', project_category),

    path('similar/<str:project_tag>', search_bar_tag),
    path('highestRate', highest_rate),
    path('search/title/<str:project_title>', search_bar_title),
    path('search/tag/<str:project_tag>', search_bar_tag),
    path('latestAdminSelected', latest_admin_selected),

    path('comments/<int:project_id>', all_comments),
]
