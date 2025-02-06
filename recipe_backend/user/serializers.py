from rest_framework import serializers
from django.contrib.auth import get_user_model
from .utils import validate_email_address


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration with password confirmation
    """
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password',},
        min_length=8,
        max_length=70
    )
    class Meta:
        model = User
        fields = [
            'email', 'password'
        ]
        
    def validate_email(self, value):
        """
        Check if email address is valid.
        """
        validate_email_address(value)
        return value

    def validate(self, data):
        """
        Check if email address is valid, and if user exists
        """
        
        if not data['email'].find('@') or not data['email'].find('.') or not data['email'].endswith('com'):
            raise serializers.ValidationError({"error": "Invalid email address. from serializers"})
        return data
    
    def create(self, validated_data):
        """
        Create and return a new user instance
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and updating user profile
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 
            'last_name', 'bio', 'profile_picture', 
            'date_of_birth', 'is_recipe_creator'
        ]
        read_only_fields = ['id', 'email']