from rest_framework import serializers
from projects.models import Categories, Tags, Projects, Pictures, Comments, Replies, Reports, Donations
from user.models import User


class getCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class getTags(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class getProjects(serializers.ModelSerializer):
    category = getCategories(read_only=True)
    tag = getTags(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = "__all__"


class createProjects(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class createComment(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class CommentReply(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = "__all__"


class ReportProject(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = "__all__"


class RateProjects(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['rate']
