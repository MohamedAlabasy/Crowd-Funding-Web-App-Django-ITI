from rest_framework import serializers
from projects.models import Categories, Rates, Tags, Projects, Pictures, Comments, ReportsComment, ReportsProject, Replies, Donations
from user.models import User


class getCategories(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class getTags(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = (
            "id",
            "tag"
        )


class getUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "mobile_phone",
            "email",
            "profile_image",
            "country",
            "Birth_date",
            "facebook_profile",
        )


class AddProjectsPictures(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'


class ProjectsPictures(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = (
            "id",
            "image"
        )


class getProjects(serializers.ModelSerializer):
    category = getCategories(read_only=True)
    tags = serializers.StringRelatedField(many=True)
    images = ProjectsPictures(many=True)
    tags = getTags(many=True)
    owner = getUser(read_only=True)

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
            "tags"
        )


class GetShortUserData(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "profile_image",
        )


class GetReplies(serializers.ModelSerializer):
    user = GetShortUserData(read_only=True)

    class Meta:
        model = Replies
        fields = (
            'id',
            "replie",
            "user",
        )


class getComments(serializers.ModelSerializer):
    user = GetShortUserData(read_only=True)
    replies = GetReplies(many=True)

    class Meta:
        model = Comments
        fields = (
            'id',
            "comment",
            "user",
            "replies",
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
        fields = (
            "title",
            "details",
            "rate",
            "current_donation",
            "total_target",
            "end_campaign",
            "category",
            "owner",
        )


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
        model = ReportsProject
        fields = "__all__"


class ReportsComment(serializers.ModelSerializer):
    class Meta:
        model = ReportsComment
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


class ProjectsTags(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class ProjectsSearchBarTags(serializers.ModelSerializer):
    project = getProjects()

    class Meta:
        model = Tags
        fields = (
            "id",
            "project"
        )
