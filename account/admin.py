from django.contrib import admin
from django.contrib.admin import register
from account.models import Profile, Pricing

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone', 'created_at')

@register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('charity', 'price')
