from rest_framework import serializers
from projects.models import Categories, Rates, Tags, Projects, Pictures, Comments, Replies, Reports, Donations
from user.models import User


class getCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class getTags(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class getUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class getProjects(serializers.ModelSerializer):
    category = getCategories(read_only=True)
    tag = getTags(many=True, read_only=True)
    owner = getUser(read_only=True)
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Projects

        fields = (
            "id",
            "title",
            "details",
            "rate",
            "total_target",
            "current_donation",
            "start_campaign",
            "end_campaign",
            "created_at",
            "selected_at_by_admin",
            "images",
            "category",
            "owner",
            "tag"
        )


class getSingleProject(serializers.ModelSerializer):
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


class DonateToProject(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__'


class updateDonateProjects(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['current_donation']


class RateProjects(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = '__all__'


class updateRateProjects(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['rate']


class ProjectsPictures(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'


class ProjectsCategoris(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsSearchBar(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
