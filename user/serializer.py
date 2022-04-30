from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from projects.models import Projects, Donations
from projects.serializers import getCategories, getTags, getProjects


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'mobile_phone', 'profile_image', 'password', 'confirm_password')

        # which data will be sent

    def create(self, validated_data):
        return User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            mobile_phone=validated_data['mobile_phone'],
            profile_image=validated_data['profile_image'],
        )

#=======================================================================================#
#			                            getUserProfile                                 	#
#=======================================================================================#


class getUserProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = [
        #     'id',
        #     'first_name',
        #     'last_name',
        #     'password',
        #     'mobile_phone',
        #     'profile_image',
        #     'Birth_date',
        #     'facebook_profile',
        #     'country'
        # ]


#=======================================================================================#
#			                            getUserProjects                                	#
#=======================================================================================#


class getUserProjects(serializers.ModelSerializer):
    owner = getUserProfile(read_only=True)
    category = getCategories(read_only=True)
    tag = getTags(many=True, read_only=True)

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


#=======================================================================================#
#			                            getUserDonations                               	#
#=======================================================================================#


class getUserDonations(serializers.ModelSerializer):
    user = getUserProfile(read_only=True)
    project = getProjects(read_only=True)

    class Meta:
        model = Donations

        fields = '__all__'
        # fields = [
        #     'id',
        #     'title',
        #     'details',
        #     'rate',
        #     'total_target',
        #     'current_donation',
        #     'start_campaign',
        #     'end_campaign',
        #     'created_at',
        #     'category',
        #     'owner',
        #     'tag',
        # ]

#=======================================================================================#
#			                               update                                   	#
#=======================================================================================#


class updateProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "password",
            "mobile_phone",
            "profile_image",
            "country",
            "Birth_date",
            "facebook_profile",
            "is_verifications",
        ]
