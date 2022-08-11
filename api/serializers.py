from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from user.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'token')
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
   
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)   
        
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        else:
            update_last_login(None, user)
        return {
        'email': user.email,
        'username': user.username,
        'token': user.token
    }
   
        
class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'last_login', 'last_request' )