from django.contrib import admin
from .models import Categories, Tags, Projects, Pictures, Comments, Replies, Reports, Donations, Rates

#=======================================================================================#
#			                           Register models                                  #
#=======================================================================================#
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Projects)
admin.site.register(Pictures)
admin.site.register(Comments)
admin.site.register(Replies)
admin.site.register(Reports)
admin.site.register(Donations)
admin.site.register(Rates)
