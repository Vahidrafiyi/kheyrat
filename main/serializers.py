from django_jalali.serializers.serializerfield import JDateTimeField
from rest_framework import serializers
from main.models import CharityList
import re

# class FastSerializer(serializers.ModelSerializer):
#     # created_at = JDateTimeField()
#     class Meta:
#         model = CharityList
#         exclude = ['prayer_sub_type']
#
#     def validate_user(self, value):
#         """
#         Check that phone number is correct
#         """
#         if value[0] == '0':
#             raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
#         if len(value) != 10:
#             raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
#         if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
#             raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
#         return value
#
# class PrayerSerializer(serializers.ModelSerializer):
#     # created_at = JDateTimeField()
#     class Meta:
#         model = CharityList
#         fields = '__all__'
#
#     def validate_user(self, value):
#         """
#         Check that phone number is correct
#         """
#         if value[0] == '0':
#             raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
#         if len(value) != 10:
#             raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
#         if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
#             raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
#         return value
#
# class QuranSerializer(serializers.ModelSerializer):
#     # created_at = JDateTimeField()
#     class Meta:
#         model = CharityList
#         exclude = ['prayer_sub_type']
#
#     def validate_user(self, value):
#         """
#         Check that phone number is correct
#         """
#         if value[0] == '0':
#             raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
#         if len(value) != 10:
#             raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
#         if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
#             raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
#         return value
#
# class SalavatSerializer(serializers.ModelSerializer):
#     # created_at = JDateTimeField()
#     class Meta:
#         model = CharityList
#         exclude = ['prayer_sub_type']
#
#     def validate_user(self, value):
#         """
#         Check that phone number is correct
#         """
#         if value[0] == '0':
#             raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
#         if len(value) != 10:
#             raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
#         if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
#             raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
#         return value

class CharitySerializer(serializers.ModelSerializer):
    purchase_code = serializers.ReadOnlyField()
    class Meta:
        model = CharityList
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