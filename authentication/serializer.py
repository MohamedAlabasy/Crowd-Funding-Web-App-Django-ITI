from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=8,write_only=True)
    confirm_password = serializers.CharField(max_length=128,min_length=8,write_only=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email','password','confirm_password','mobile_phone')
        # which data will be sent 
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)