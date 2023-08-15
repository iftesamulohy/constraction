from rest_framework import serializers

from loan.models import LoanBeneficaries, LoanTransactions

class LoanBeneficariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanBeneficaries
        fields = '__all__'
class LoanTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanTransactions
        fields = ['id','giver_id','taker_id','amount','interest','return_type','instalment','status']