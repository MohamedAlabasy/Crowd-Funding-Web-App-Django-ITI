from django.contrib import admin
from .models import Projects, Categories, Tags, Projects, Pictures, Comments, Replies, ReportsComment, ReportsProject, Donations, Rates

#=======================================================================================#
#			                           Register models                                  #
#=======================================================================================#
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Pictures)
admin.site.register(Comments)
admin.site.register(Replies)
admin.site.register(ReportsProject)
admin.site.register(ReportsComment)
admin.site.register(Donations)
admin.site.register(Rates)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display =('title','category','created_at')
    ordering=('title',)
    search_fields=('title','category')