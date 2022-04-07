from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from account.models import Profile
from account.serializers import ProfileSerializer


class CurrentUserProfile(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.filter(user=user)
        return profile
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
