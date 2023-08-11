from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from loan.models import LoanBeneficaries
from loan.serializers import LoanBeneficariesSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.views import IsStaff
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
    