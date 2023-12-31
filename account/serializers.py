from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=3, max_length=25, write_only=True)
    password2 = serializers.CharField(min_length=3, max_length=25, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'password2', 'full_name', 'phone', 'image', 'bio')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password does not same, Try again!')
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=221, required=True)
    password = serializers.CharField(max_length=25, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        username = obj.get('username')
        tokens = Account.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                "message": "Username or password not correct"
            })
        if not user.is_active:
            raise AuthenticationFailed({
                "message": "Account disabled"
            })
        return attrs


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'full_name', 'image_tag', 'bio', 'date_created', 'date_modified']


