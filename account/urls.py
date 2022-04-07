from django.urls import path
from account.views import CurrentUserProfile, Notification, AllCharity

urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
    path('notification/', Notification.as_view()),
    path('all-charity/', AllCharity.as_view()),
]