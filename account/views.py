import datetime

from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Profile
from account.serializers import ProfileSerializer
from main.models import CharityList
from main.serializers import CharitySerializer


class CurrentUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query)
        return Response(serializer.data, status=200)

class Notification(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = CharityList.objects.filter(accepted=False)
        if len(query) > 3:
            query = query[len(query)-3:len(query)]
        serializer = CharitySerializer(query, many=True)
        return Response(serializer.data, status=200)

class UnAcceptedCharityList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = CharityList.objects.filter(accepted=False)
        serializer = CharitySerializer(query, many=True)
        return Response(serializer.data, status=200)

class AcceptCharity(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, pk):
        charity = CharityList.objects.get(pk=pk)
        charity.accepted = True
        user = Profile.objects.get(user_id=request.user.id)
        fast_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='روزه').aggregate(sum=Sum('quantity'))
        prayer_aggregate = CharityList.objects.filter(Q(acceptor=request.user , charity_type='نماز واجب') | Q(acceptor=request.user , charity_type='نماز مستحب') | Q(acceptor=request.user , charity_type='یک روز کامل')).aggregate(sum=Sum('quantity'))
        salavat_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='صلوات').aggregate(sum=Sum('quantity'))
        quran_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='قرآن').aggregate(sum=Sum('quantity'))

        if charity.charity_type == 'روزه':
            if fast_aggregate != None and fast_aggregate['sum'] >= 60:
                return Response({'error': 'سهمیه ی روزه شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.fast += charity.quantity
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'نماز واجب' or charity.charity_type == 'نماز مستحب' or charity.charity_type == 'یک روز کامل':
            if prayer_aggregate != None and prayer_aggregate['sum'] >= 700:
                return Response({'error': 'سهمیه ی نماز شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.prayer += charity.quantity
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'جزء' or charity.charity_type == 'ختم':
            if quran_aggregate != None and quran_aggregate['sum'] >= 144:
                return Response({'error': 'سهمیه ی قرآن شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.quran += charity.quantity
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'صلوات':
            if salavat_aggregate != None and salavat_aggregate['sum'] >= 10000:
                return Response({'error': 'سهمیه ی صلوات شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.salavat += charity.quantity
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        charity.save()
        user.save()
        return Response({'result':'charity accepted'}, status=200)
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

class DoneCharity(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        charity = CharityList.objects.get(pk=pk)
        user = Profile.objects.get(user_id=request.user.id)
        if charity.charity_type == 'روزه':
            user.fast -= charity.quantity

        if charity.charity_type == 'نماز واجب' or charity.charity_type == 'نماز مستحب' or charity.charity_type == 'یک روز کامل':
            user.prayer -= charity.quantity

        if charity.charity_type == 'جزء' or charity.charity_type == 'ختم':
            user.quran -= charity.quantity

        if charity.charity_type == 'صلوات':
            user.salavat -= charity.quantity

        charity.save()
        user.save()
        return Response({'result':'charity done'}, status=200)
