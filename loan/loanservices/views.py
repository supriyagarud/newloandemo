from django.shortcuts import render
import requests
# Create your views here.
from rest_framework import status
from .serializers import LoanSerializers, TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .models import Loan,Customer,Transact
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.decorators import api_view





@api_view(['GET', 'POST'])
def loan_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        print("hi")
        products = Loan.objects.all()
        serializer = LoanSerializers(products,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        '''
        print("post method data",request.data)
        serializer = LoanSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''

        '''
            {
    "loan_id": 2, 'loan_id': request.data.get('loan_id'),
    "cust_id": 102,
    "loan_acc_no": 58906,
    "loan_type": "V",
    "total_loan": "a"
  },
  
  
  t_serializer = TransactionSerializer(data=new_data)
            if t_serializer.is_valid():
                print("hi post")
                transaction = t_serializer.save()
                print("hi,post")
                return Response(t_serializer.data, status=status.HTTP_201_CREATED)
        '''
        data_old = {
                    'cust_id': request.data.get('cust_id'),
                    'loan_acc_no': request.data.get('loan_acc_no'),
                    'loan_type': request.data.get('loan_type'),
                    'total_loan': request.data.get('total_loan')}
        print(data_old)
        if Customer.account_balance< 500000:
           return Response("Not applicable")
        serializer = LoanSerializers(data=data_old)
        #loan_type={'a':1000,'b':2000,'c':5000}
        if serializer.is_valid():

            insurance = serializer.save()
            new_data = {'cust_id': request.data.get('cust_id')}
            print(new_data)

            t_serializer = TransactionSerializer(data={'loan':insurance.pk, 'cust_id':request.data.get('cust_id')})
            if t_serializer.is_valid():
                print("hi tranct")
                transaction = t_serializer.save()
                print("hi,tranct")
                return Response(t_serializer.data, status=status.HTTP_201_CREATED)

            #Customer.account_balance =Customer.account_balance+loan_type[request.data.get('total_loan')]
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def loan_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:

        product = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanSerializers(product,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("updated data",request.data)
        serializer = LoanSerializers(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tranct_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        print(" Tranct hi")
        products = Transact.objects.all()
        serializer = LoanSerializers(products,context={'request': request} ,many=True)
        return Response(serializer.data)
