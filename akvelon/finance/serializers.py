from rest_framework import serializers
from .models import User, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'date']


class SumTransactionByDateSerializer(serializers.Serializer):
    date = serializers.DateField()
    sum = serializers.FloatField()
