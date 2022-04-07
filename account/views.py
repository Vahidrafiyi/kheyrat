from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Profile
from account.serializers import ProfileSerializer
from main.models import CharityList
from main.serializers import CharityListSerializer


class CurrentUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query)
        return Response(serializer.data, status=200)

class Notification(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        query = CharityList.objects.all()

        if len(query) > 3:
            query = query[len(query)-3:len(query)]
        serializer = CharityListSerializer(query, many=True)
        return Response(serializer.data, status=200)

class AllCharity(APIView):
    def get(self, request):
        query = CharityList.objects.all()
        serializer = CharityListSerializer(query, many=True)
        return Response(serializer.data, status=200)
