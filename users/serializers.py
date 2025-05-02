# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         ref_name = 'CustomUser'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import User
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        data = super().validate({
            "username": user.username,
            "password": password,
            "first_name":first_name,
            "last_name":last_name,
            "role": role, 
        })

        data["user_id"] = user.id
        data["email"] = user.email
        return data



# User = get_user_model()

# ACCOUNT_TYPE_CHOICES = ['client', 'administrator', 'technician']

# class RegisterSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)
#     account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'account_type']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Passwords do not match.")
#         validate_password(data['password'])
#         return data

#     def create(self, validated_data):
#         validated_data.pop('confirm_password')
#         user = User.objects.create_user(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             account_type=validated_data['account_type'],
#         )
#         return user


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('client', 'Client'), ('administrator', 'Administrator'), ('technician', 'Technician')])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'role']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']