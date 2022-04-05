from django.urls import path

from main.views import FastAPI, PrayerAPI, QuranAPI, SalavatAPI

urlpatterns = [
    path('fast/', FastAPI.as_view()),
    path('prayer/', PrayerAPI.as_view()),
    path('quran/', QuranAPI.as_view()),
    path('salavat/', SalavatAPI.as_view()),
]