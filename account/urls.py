from django.urls import path
from account.views import CurrentUserProfile
urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
]