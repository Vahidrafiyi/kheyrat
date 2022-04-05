from django.contrib import admin
from django.contrib.admin import register
from main.models import Fast, Quran, Prayer, Salavat


@register(Prayer)
class PrayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'how_many', 'created_at', 'done')


@register(Fast)
class FastAdmin(admin.ModelAdmin):
    list_display = ('user', 'how_many', 'created_at', 'done')


@register(Quran)
class QuranAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'how_many', 'created_at', 'done')

@register(Salavat)
class SalavatAdmin(admin.ModelAdmin):
    list_display = ('user', 'how_many', 'created_at', 'done')
