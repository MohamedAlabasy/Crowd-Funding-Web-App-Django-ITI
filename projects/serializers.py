from rest_framework import serializers
from projects.models import Categories, Tags, Projects, Pictures, Comments, Replies, Reports, Donations
from user.models import User

#=======================================================================================#
#			                            Categories                                     	#
#=======================================================================================#


class getCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"

#=======================================================================================#
#			                               Tags                                     	#
#=======================================================================================#


class getTags(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"
        # fields = [
        #     "id",
        #     "name"
        # ]
#=======================================================================================#
#			                            0                                     	#
#=======================================================================================#
