from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from loan.models import LoanBeneficaries
from loan.serializers import LoanBeneficariesSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.views import IsStaff
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework.response import Response
# All Filter Views here
class LoanBenfcaiesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    giver_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanBeneficaries
        fields = ['first_name','last_name','email','giver_name']  # Add more fields if needed
# Create your views here.
class AllLoanBeneficaries(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = LoanBeneficariesSerializer
    queryset = LoanBeneficaries.objects.all()
    pagination_class = LimitOffsetPagination
    # page_size = 10  # Number of items per page
    # page_size_query_param = 'page_size'  # Custom query parameter for changing page size
    # max_page_size = 100  # Maximum page size allowed
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = LoanBenfcaiesFilter  # Use the custom filter class
    def get_queryset(self):
        return LoanBeneficaries.objects.filter(is_deleted=False)
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Loan Beneficaries deleted. But you can recover your data"})
    