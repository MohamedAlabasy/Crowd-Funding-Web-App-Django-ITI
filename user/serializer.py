from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=8,write_only=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email','password','mobile_phone')
        # which data will be sent 
    def create(self, validated_data):
        
        return User.objects.create( 
            first_name  = validated_data['first_name'],
            last_name  = validated_data['last_name'],
            email = validated_data['email'],
            password = make_password(validated_data['password']),
            mobile_phone = validated_data['mobile_phone']
            )