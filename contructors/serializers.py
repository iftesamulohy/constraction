from rest_framework import serializers
from contructors.models import ContructorsBeneficaries
from loan.serializers import PhoneSerializer


class ContructorsBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = ContructorsBeneficaries
        fields = '__all__'