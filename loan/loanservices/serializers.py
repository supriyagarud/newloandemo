from rest_framework import serializers
from .models import Loan,Transact


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transact
        fields = '__all__'


class LoanSerializers(serializers.ModelSerializer):
    tranctions=TransactionSerializer(many=True,read_only=True,required=False)
    class Meta :
        model = Loan
        fields ="__all__"
