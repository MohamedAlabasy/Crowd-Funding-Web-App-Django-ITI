import re
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from django.contrib.auth.hashers import make_password
from projects.models import Projects, Donations
from projects.serializers import getCategories, getTags, getProjects
from user.passwordResetToken import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True)
    confirm_password = serializers.CharField(
        write_only=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'mobile_phone', 'profile_image', 'password', 'confirm_password')

    def validate(self, attrs):
        password = attrs.get('password', '')
        match = re.fullmatch(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$", password)
        if not match:
            raise serializers.ValidationError(
                {'password': 'The password should be 8 length and at least one upper case, one lower case, one special character and one digit'})
        return attrs

    def create(self, validated_data):
        return User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            mobile_phone=validated_data['mobile_phone'],
            profile_image=validated_data['profile_image']
        )


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta():
        model = User
        fields = ('email', 'password', 'id', 'token', 'first_name', 'last_name', 'mobile_phone',
                  'profile_image', 'country', 'Birth_date', 'facebook_profile', 'is_verifications')
        read_only_fields = ['token', 'id', 'first_name', 'last_name', 'mobile_phone',
                            'profile_image', 'country', 'Birth_date', 'facebook_profile', 'is_verifications']


###########Email Verify ##################
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta():
        model = User
        fields = ['token']
####################################Reset password###############


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['new_password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            new_password = attrs.get('new_password')

            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user2 = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user2, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            print(new_password, id)
            user2.password = make_password(new_password)
            print(user2)

            user2.save()

            return (user2)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
#=======================================================================================#
#			                            getUserProfile                                 	#
#=======================================================================================#


class getUserProfile(serializers.ModelSerializer):
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

#=======================================================================================#
#			                            getUserProjects                                	#
#=======================================================================================#


class getUserProjects(serializers.ModelSerializer):
    owner = getUserProfile(read_only=True)
    category = getCategories(read_only=True)
    tags = serializers.StringRelatedField(many=True)
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
            "tags"
        )


#=======================================================================================#
#			                            getUserDonations                               	#
#=======================================================================================#


class getUserDonations(serializers.ModelSerializer):
    user = getUserProfile(read_only=True)
    project = getProjects(read_only=True)

    class Meta:
        model = Donations

        fields = '__all__'

#=======================================================================================#
#			                               update                                   	#
#=======================================================================================#


class updateProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "mobile_phone",
            "profile_image",
            "country",
            "Birth_date",
            "facebook_profile",
        ]
