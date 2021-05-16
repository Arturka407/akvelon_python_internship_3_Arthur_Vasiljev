from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer, SumTransactionByDateSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['amount', 'date']

    def get_queryset(self):
        queryset = Transaction.objects.all()
        transaction_type = self.request.query_params.get('transactionType')
        if transaction_type is not None:
            if transaction_type == 'income':
                queryset = queryset.exclude(amount__contains='-')
            elif transaction_type == 'outcome':
                queryset = queryset.filter(amount__contains='-')
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionViewList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SumTransactionViewGroupedByDate(generics.ListAPIView):
    queryset = Transaction.objects.values('date').order_by('date').annotate(sum=Sum('amount'))
    serializer_class = SumTransactionByDateSerializer

