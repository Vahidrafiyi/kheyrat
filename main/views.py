from itertools import chain

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Profile
from account.serializers import ProfileSerializer
from main.models import Fast, Prayer, Quran, CharityList, Salavat
from main.serializers import FastSerializer, PrayerSerializer, QuranSerializer, SalavatSerializer, CharityListSerializer


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

class CharityUnAcceptedList(APIView):
    # def get(self, request):
    #     query_set = CharityList.objects.filter(accepted=False)
    #     serializer = CharityListSerializer(query_set, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        print(request.user)
        # print(request.user.id)
        charity = CharityList.objects.get(pk=pk)
        print(charity.quantity)
        print(charity.accepted)
        charity.accepted = True
        print(charity.accepted)
        user = Profile.objects.get(user_id=request.user.id)
        if charity.charity_type == 'fast':
            user.fast += charity.quantity
        if charity.charity_type == 'prayer':
            user.prayer += charity.quantity
        if charity.charity_type == 'quran':
            user.quran += charity.quantity
        if charity.charity_type == 'salavat':
            user.salavat += charity.quantity
        user.save()
        charity.delete()
        # serializer = ProfileSerializer(user)
        return Response({'result':'accepted'}, status=200)
        # queryset_a = Fast.objects.all()
        # queryset_b = Prayer.objects.all()
        # queryset_c = Salavat.objects.all()
        # queryset_d = Quran.objects.all()
        #
        # # Create an iterator for the querysets and turn it into a list.
        # results_list = list(chain(queryset_a, queryset_b, queryset_c, queryset_d))
        #
        # # Build the list with items based on the FeedItemSerializer fields
        # results = {}
        # new_list = {'fast':[], 'salavat':[], 'prayer':[], 'quran':[]}
        # for entry in results_list:
        #     item_type = entry.__class__.__name__.lower()
        #     if isinstance(entry, Fast):
        #         serializer = FastSerializer(entry)
        #         new_list['fast'].append(serializer.data)
        #     if isinstance(entry, Prayer):
        #         serializer = PrayerSerializer(entry)
        #         new_list['prayer'].append(serializer.data)
        #     if isinstance(entry, Salavat):
        #         serializer = SalavatSerializer(entry)
        #         new_list['salavat'].append(serializer.data)
        #     if isinstance(entry, Quran):
        #         serializer = QuranSerializer(entry)
        #         new_list['quran'].append(serializer.data)
        #     results[item_type] = new_list[item_type]
        # # print(new_list['fast'])
        # return Response(results, status=200)

