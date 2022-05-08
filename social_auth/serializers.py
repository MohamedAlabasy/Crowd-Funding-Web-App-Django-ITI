from rest_framework import serializers
from user.models import User


class FacebookSocialAuthSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField()
    class Meta():
            model = User
            fields = ['auth_token']
