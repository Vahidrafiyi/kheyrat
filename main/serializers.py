from rest_framework import serializers
from main.models import Fast, Prayer, Quran, Salavat
import re
from django_jalali.serializers.serializerfield import JDateTimeField

class FastSerializer(serializers.ModelSerializer):
    # created_at = JDateTimeField()
    class Meta:
        model = Fast
        fields = '__all__'

    def validate_user(self, value):
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

class PrayerSerializer(serializers.ModelSerializer):
    # created_at = JDateTimeField()
    class Meta:
        model = Prayer
        fields = '__all__'

    def validate_user(self, value):
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

class QuranSerializer(serializers.ModelSerializer):
    # created_at = JDateTimeField()
    class Meta:
        model = Quran
        fields = '__all__'

    def validate_user(self, value):
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

class SalavatSerializer(serializers.ModelSerializer):
    # created_at = JDateTimeField()
    class Meta:
        model = Salavat
        fields = '__all__'

    def validate_user(self, value):
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