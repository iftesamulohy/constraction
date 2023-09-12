from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.models import Beneficaries, PhoneNumber
from globalapp2.views import BaseViews
from loan.models import LoanBeneficaries, LoanInstallment, LoanTransactions
from loan.serializers import LoanBeneficariesSerializer, LoanInstallmenttionSerializer, LoanTransactionSerializer, PhoneSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.views import IsStaff
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# All Filter Views here
class LoanBenfcaiesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    giver_name = django_filters.CharFilter(lookup_expr='icontains')
    NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanBeneficaries
        fields = ['first_name','last_name','email','giver_name','NID_number']  # Add more fields if needed


class LoanTransactionsFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    giver_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__email = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__email = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanTransactions
        fields = ['giver_id__first_name','giver_id__last_name','giver_id__email','giver_id__NID_number','taker_id__first_name','taker_id__last_name','taker_id__email','taker_id__NID_number']  # Add more fields if needed

        #Phone Filter
class PhoneFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    role__first_name = django_filters.CharFilter(lookup_expr='icontains')
    role__last_name = django_filters.CharFilter(lookup_expr='icontains')
    ben_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    ben_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    phone_number =django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PhoneNumber
        fields = ['role__first_name','role__last_name','ben_id__first_name','ben_id__last_name','phone_number']  # Add more fields if needed
# Create your views here.
class AllLoanBeneficaries(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = LoanBeneficariesSerializer
    queryset = LoanBeneficaries.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = LoanBenfcaiesFilter  # Use the custom filter class
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        item = self.get_object()
        item.status = not item.status
        item.save()
        return Response({"message": "Status changed"})
    def get_queryset(self):
        return LoanBeneficaries.objects.filter(is_deleted=False)
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Loan Beneficaries deleted. But you can recover your data"})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        phone_numbers = serializer.initial_data['phone_number']
        
        for phone_number in phone_numbers:
            print(phone_number)
            print(type(phone_number['role']))
            PhoneNumber.objects.create(
                name= phone_number['name'],
                relation= phone_number['relation'],
                phone_number= phone_number['phone_number'],
                status= True,
                role= Beneficaries.objects.get(id=phone_number['role']),
                ben_id= Beneficaries.objects.get(id=phone_number['ben_id'])

            )
        new_data = {key: value for key, value in serializer.initial_data.items() if key != "phone_number"}
        data=new_data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message":"Loan Beneficaries Created",
            "data":serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
        #return Response({"message": "data check done"})

class AllLoanTransactions(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = LoanTransactionSerializer
    queryset = LoanTransactions.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = LoanTransactionsFilter  # Use the custom filter class
    def get_queryset(self):
        return LoanTransactions.objects.filter(is_deleted=False)
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Loan Transactions deleted. But you can recover your data"})
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        item = self.get_object()
        item.status = not item.status
        item.save()
        return Response({"message": "Status changed"})
class PhoneViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = PhoneSerializer
    queryset = PhoneNumber
    model_name=PhoneNumber
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = PhoneFilter # Use the custom filter class

class LoanInstallmentViews(BaseViews):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = LoanInstallmenttionSerializer
    queryset = LoanInstallment
    model_name=LoanInstallment
    pagination_class = LimitOffsetPagination
    #filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = PhoneFilter # Use the custom filter class


