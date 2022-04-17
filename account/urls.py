from django.urls import path, re_path
from account.views import CurrentUserProfile, Notification, UnAcceptedCharityList, AcceptCharity, DoneCharity, \
    RegisterAPI, UserPurchaseAPI, AdminProfile, AdminPurchase

urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
    path('notification/', Notification.as_view()),
    path('unaccepted_charities/', UnAcceptedCharityList.as_view()),
    path('accept/<int:pk>', AcceptCharity.as_view()),
    path('done/<int:pk>', DoneCharity.as_view()),
    path('all_purchase/<str:phone>', UserPurchaseAPI.as_view()),
    path('admin/profile/', AdminProfile.as_view()),
    re_path(r'admin/purchase/$', AdminPurchase.as_view()),
    re_path(r'admin/profile/(?P<pk>[0-9]+)$', AdminProfile.as_view()),
    # path('admin/search/<str:search_by>/<str:search_t>', SearchPurchaseAPI.as_view()),
    # path('admin/profile/<str:search_by>/<str:search_t>', SearchUserAPI.as_view()),
]