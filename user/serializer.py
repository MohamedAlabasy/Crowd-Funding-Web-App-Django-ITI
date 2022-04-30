from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from projects.models import Projects
# from projects.serializers import Projects


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',
                  'mobile_phone', 'profile_image', 'confirm_password')
        extra_kwargs = {
            "confirm_password": {"required": False}
        }
        # which data will be sent

    def create(self, validated_data):
        # print(validated_data['confirm_password']==validated_data['confirm_password'])
        return User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            mobile_phone=validated_data['mobile_phone'],
            profile_image=validated_data['profile_image'],
        )


class viewUserProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            'id',
            'first_name',
            'last_name',
            'password',
            'mobile_phone',
            'profile_image',
            'Birth_date',
            'facebook_profile',
            # 'country'
        ]


class viewUserProjects(serializers.ModelSerializer):
    owner = viewUserProfile(read_only=True)
    # category = viewUserProfile(read_only=True)
    # tag = viewUserProfile(many=true,read_only=True)

    class Meta:
        model = Projects
        fields = [
            'id',
            'title',
            'details',
            'rate',
            'total_target',
            'current_donation',
            'start_campaign',
            'end_campaign',
            'created_at',
            'category',
            'owner',
            'tag',
        ]
