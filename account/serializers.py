from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from account.models import Profile
import re

class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerialzier()
    class Meta:
        model = Profile
        fields = ['user', 'phone', 'gender', 'image','created_at']
        depth = 1

    def update(self, instance, validated_data):
        print(validated_data)
        # user_data = validated_data.pop('user')
        # user = instance.user
        # print(user_data.get('first_name'))

        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()

        # user.username = user_data.get('username', user.username)
        instance.user.first_name = validated_data['user'].get('first_name', instance.user.first_name)
        # user.last_name = user_data.get('last_name', user.last_name)
        # print(user_data.get('first_name'))
        instance.user.save()
        return instance

    def validate_phone(self, value):
        """
        Check that phone number is correct
        """
        if value[0] == '0':
            raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
        if len(value) != 10:
            raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
        if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
            raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
        return value

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password], required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'passwords must be match!'})

        return attrs

    def validate_username(self, value):
        """
        Check that phone number is correct
        """
        if value[0] == '0':
            raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
        if len(value) != 10:
            raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
        if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
            raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
        return value

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

