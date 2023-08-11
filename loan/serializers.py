from rest_framework import serializers

from loan.models import LoanBeneficaries

class LoanBeneficariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanBeneficaries
        fields = '__all__'