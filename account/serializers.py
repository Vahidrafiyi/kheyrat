from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Profile
import re
class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerialzier
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'gender', 'image','created_at']
        depth = 1

    # def update(self, instance, validated_data):
    #     instance.user.first_name = validated_data.get('first_name', instance.user.first_name)
    #     # validated_data['last_name'] = self.last_name
    #     # instance.save()
    #     # super().update(instance, validated_data)
    #     instance.save()
    #     return instance
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
