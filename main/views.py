from itertools import chain

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Profile
from account.serializers import ProfileSerializer
from main.models import CharityList
from main.serializers import CharitySerializer


class CharityAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PrayerAPI(APIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     def post(self, request):
#         serializer = PrayerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class QuranAPI(APIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     def post(self, request):
#         serializer = QuranSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SalavatAPI(APIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     def post(self, request):
#         serializer = SalavatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



