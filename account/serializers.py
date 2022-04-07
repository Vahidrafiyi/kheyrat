from rest_framework import serializers
from account.models import Profile
import re

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    fast = serializers.ReadOnlyField()
    salavat = serializers.ReadOnlyField()
    prayer = serializers.ReadOnlyField()
    quran = serializers.ReadOnlyField()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'phone', 'gender', 'image',
                  'fast', 'salavat', 'prayer', 'quran', 'created_at']

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
