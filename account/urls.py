from django.urls import path
from account.views import CurrentUserProfile, Notification, UnAcceptedCharityList, AcceptCharity, DoneCharity

urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
    path('notification/', Notification.as_view()),
    path('unaccepted_charities/', UnAcceptedCharityList.as_view()),
    path('accept/<int:pk>/', AcceptCharity.as_view()),
    path('done/<int:pk>/', DoneCharity.as_view()),
]