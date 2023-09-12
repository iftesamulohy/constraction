from rest_framework import serializers
from globalapp2.models import PhoneNumber

from loan.models import LoanBeneficaries, LoanInstallment, LoanTransactions
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'
class LoanBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = LoanBeneficaries
        fields = '__all__'
class LoanTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanTransactions
        fields = '__all__'
class LoanInstallmenttionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanInstallment
        fields = '__all__'

