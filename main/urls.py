from django.urls import path

from main.views import CharityAPI

urlpatterns = [
    path('charity/', CharityAPI.as_view()),
]