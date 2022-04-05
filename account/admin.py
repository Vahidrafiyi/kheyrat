from django.contrib import admin
from django.contrib.admin import register
from account.models import Profile

@register(Profile)
class SalavatAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'created_at')
