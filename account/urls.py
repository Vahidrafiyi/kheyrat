from django.urls import path, re_path
from account.views import CurrentUserProfile, Notification, UnAcceptedCharityList, AcceptCharity, DoneCharity, \
    RegisterAPI, UserPurchaseAPI, AdminProfile

urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
    path('notification/', Notification.as_view()),
    path('unaccepted_charities/', UnAcceptedCharityList.as_view()),
    path('accept/<int:pk>', AcceptCharity.as_view()),
    path('done/<int:pk>', DoneCharity.as_view()),
    path('all_purchase/<str:phone>', UserPurchaseAPI.as_view()),
    re_path(r'admin/profile/$', AdminProfile.as_view()),
    re_path(r'admin/profile/(?P<pk>[0-9]+)$', AdminProfile.as_view()),
]