from django.urls import path

from main.views import FastAPI, PrayerAPI, QuranAPI, SalavatAPI, CharityUnAcceptedList

urlpatterns = [
    path('fast/', FastAPI.as_view()),
    path('prayer/', PrayerAPI.as_view()),
    path('quran/', QuranAPI.as_view()),
    path('salavat/', SalavatAPI.as_view()),
    path('accept/<int:pk>', CharityUnAcceptedList.as_view()),
]