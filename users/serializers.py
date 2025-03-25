from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
import re


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError('Incorrect usernanme or password')
  

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, old_password):
        user = self.context['user']
        if not check_password(old_password, user.password):
            raise serializers.ValidationError(
                'Invalid password entered'
            )
        return old_password

    def validate_password(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{8,}$"
        if not re.match(pattern, password):
            raise serializers.ValidationError(
                'Password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit and one special character'
                )            
        return password