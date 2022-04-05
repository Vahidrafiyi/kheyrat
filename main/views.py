from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Fast, Prayer, Quran
from main.serializers import FastSerializer, PrayerSerializer, QuranSerializer, SalavatSerializer


class FastAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        serializer = FastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrayerAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        serializer = PrayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuranAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        serializer = QuranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalavatAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        serializer = SalavatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)