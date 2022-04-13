from django.contrib import admin
from django.contrib.admin import register
from main.models import CharityList


# @register(Prayer)
# class PrayerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'type', 'how_many', 'created_at', 'done')
#
#
# @register(Fast)
# class FastAdmin(admin.ModelAdmin):
#     list_display = ('user', 'how_many', 'created_at', 'done')
#
#
# @register(Quran)
# class QuranAdmin(admin.ModelAdmin):
#     list_display = ('user', 'type', 'how_many', 'created_at', 'done')
#
# @register(Salavat)
# class SalavatAdmin(admin.ModelAdmin):
#     list_display = ('user', 'how_many', 'created_at', 'done')

@register(CharityList)
class CharityListAdmin(admin.ModelAdmin):
    list_display = ('charity_type', 'user', 'quantity', 'accepted', 'acceptor', 'when_accepted', 'done')
