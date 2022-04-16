import datetime

from django.contrib.auth.models import User
from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Profile
from account.permissions import IsAdminUser
from account.serializers import ProfileSerializer, RegisterSerializer
from main.models import CharityList
from main.serializers import CharitySerializer


class CurrentUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query)
        return Response(serializer.data, status=200)

    def patch(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Notification(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = CharityList.objects.filter(accepted=False)
        fast_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='روزه').aggregate(sum=Sum('quantity'))
        prayer_aggregate = CharityList.objects.filter(
            Q(acceptor=request.user, charity_type='نماز واجب') | Q(acceptor=request.user,
            charity_type='نماز مستحب') | Q(acceptor=request.user,charity_type='یک روز کامل')).aggregate(sum=Sum('quantity'))
        salavat_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='صلوات').aggregate(sum=Sum('quantity'))
        quran_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='قرآن').aggregate(sum=Sum('quantity'))
        print(query)
        query_set = []
        for instance in query:
            if instance.charity_type == 'روزه' and fast_aggregate['sum'] != None and fast_aggregate['sum'] >= 60:
                pass

            elif (instance.charity_type == 'نماز واجب' or instance.charity_type == 'نماز مستحب' or instance.charity_type == 'یک روز کامل')\
                    and prayer_aggregate['sum'] != None and prayer_aggregate['sum'] >= 700 :
                pass

            elif (instance.charity_type == 'ختم' or instance.charity_type == 'جزء') and quran_aggregate['sum'] != None and quran_aggregate['sum'] >= 144 :
                pass

            elif instance.charity_type == 'صلوات' and salavat_aggregate['sum'] != None and salavat_aggregate['sum'] >= 10000 :
                pass

            else:
                query_set.append(instance)
        print(query_set)
        if len(query_set) > 3:
            query_set = query_set[len(query_set)-3:len(query_set)]

        serializer = CharitySerializer(query_set, many=True)
        return Response(serializer.data, status=200)

class UnAcceptedCharityList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        query = CharityList.objects.filter(accepted=False)
        serializer = CharitySerializer(query, many=True)
        return Response(serializer.data, status=200)

class AcceptCharity(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        charity = CharityList.objects.get(pk=pk)
        user = Profile.objects.get(user_id=request.user.id)
        fast_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='روزه').aggregate(sum=Sum('quantity'))
        prayer_aggregate = CharityList.objects.filter(Q(acceptor=request.user , charity_type='نماز واجب') | Q(acceptor=request.user , charity_type='نماز مستحب') | Q(acceptor=request.user , charity_type='یک روز کامل')).aggregate(sum=Sum('quantity'))
        salavat_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='صلوات').aggregate(sum=Sum('quantity'))
        quran_aggregate = CharityList.objects.filter(acceptor=request.user, charity_type='قرآن').aggregate(sum=Sum('quantity'))

        if charity.charity_type == 'روزه':
            if fast_aggregate != None and fast_aggregate['sum'] >= 60:
                return Response({'error': 'سهمیه ی روزه شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'نماز واجب' or charity.charity_type == 'نماز مستحب' or charity.charity_type == 'یک روز کامل':
            if prayer_aggregate != None and prayer_aggregate['sum'] >= 700:
                return Response({'error': 'سهمیه ی نماز شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'جزء' or charity.charity_type == 'ختم':
            if quran_aggregate != None and quran_aggregate['sum'] >= 144:
                return Response({'error': 'سهمیه ی قرآن شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        if charity.charity_type == 'صلوات':
            if salavat_aggregate != None and salavat_aggregate['sum'] >= 10000:
                return Response({'error': 'سهمیه ی صلوات شما تمام شده است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            charity.accepted = True
            charity.acceptor = request.user
            charity.when_accepted = datetime.datetime.now()
        charity.save()
        user.save()
        return Response({'result':f'{charity.charity_type} accepted'}, status=200)
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
        charity.done = True
        charity.save()
        user.save()
        return Response({'result' : f'{charity.charity_type} done'}, status=200)

# class CurrentUserCharity(APIView):
#     def get(self, request):

class RegisterAPI(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserPurchaseAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, phone):
        query_set = CharityList.objects.filter(user=phone)
        serializer = CharitySerializer(query_set, many=True)
        return Response(serializer.data, status=200)

class AdminProfile(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        query_set = Profile.objects.all()
        serializer = ProfileSerializer(query_set, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        query = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        query = Profile.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminPurchase(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        query_set = CharityList.objects.all()
        serializer = CharitySerializer(query_set, many=True)
        return Response(serializer.data, status=200)

class SearchPurchaseAPI(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, search_by, search_t):
        if search_by == 'user':
            query = CharityList.objects.filter(user__icontains=search_t)

        elif search_by == 'purchase_code':
            query = CharityList.objects.filter(purchase_code__icontains=search_t)

        elif search_by == 'mentioned_info':
            query = CharityList.objects.filter(mentioned_info__icontains=search_t)

        elif search_by == 'charity_type':
            query = CharityList.objects.filter(charity_type__icontains=search_t)

        elif search_by == 'acceptor':
            query = CharityList.objects.filter(acceptor__username__icontains=search_t)

        serializer = CharitySerializer(query, many=True)
        return Response(serializer.data, status=200)

class SearchUserAPI(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, search_by, search_t):
        if search_by == 'username':
            query = Profile.objects.filter(user__username__icontains=search_t)

        elif search_by == 'phone':
            query = Profile.objects.filter(phone__icontains=search_t)

        elif search_by == 'code_melli':
            query = Profile.objects.filter(code_melli__icontains=search_t)

        serializer = ProfileSerializer(query, many=True)
        return Response(serializer.data, status=200)


