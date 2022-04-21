from itertools import chain

import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import Profile, Pricing
from account.serializers import ProfileSerializer
from main.models import CharityList
from main.serializers import CharitySerializer

logger = logging.getLogger(__name__)


class CharityAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CharitySerializer(data=request.data)
        charity = Pricing.objects.get(
            Q(charity=request.data['charity_type']) | Q(charity=request.data['prayer_sub_type']))
        final_price = int(charity.price) * int(request.data['quantity'])
        print(final_price)
        tax = (float(final_price) * 0.09)
        print(tax)
        final_price_with_tax = final_price + tax
        print(final_price_with_tax)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'final_price_with_tax': final_price_with_tax},
                            status=status.HTTP_201_CREATED)
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
