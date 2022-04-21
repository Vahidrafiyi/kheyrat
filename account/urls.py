from django.urls import path, re_path
from account.views import CurrentUserProfile, Notification, UnAcceptedCharityList, AcceptCharity, DoneCharity, \
    RegisterAPI, UserPurchaseAPI, AdminProfile, AdminPurchase, AddAdmin, PricingAPI

urlpatterns = [
    path('profile/', CurrentUserProfile.as_view()),
    path('notification/', Notification.as_view()),
    path('unaccepted-charities/', UnAcceptedCharityList.as_view()),
    path('accept/<int:pk>', AcceptCharity.as_view()),
    path('done/<int:pk>', DoneCharity.as_view()),
    path('all-purchase/<str:phone>', UserPurchaseAPI.as_view()),
    path('admin/profile/', AdminProfile.as_view()),
    re_path(r'admin/purchase/$', AdminPurchase.as_view()),
    re_path(r'admin/profile/(?P<pk>[0-9]+)$', AdminProfile.as_view()),
    path('admin/add-admin/<int:pk>', AddAdmin.as_view()),
    re_path(r'admin/pricing/$', PricingAPI.as_view()),
    re_path(r'admin/pricing/(?P<pk>[0-9]+)$', PricingAPI.as_view()),
]