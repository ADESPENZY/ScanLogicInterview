from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_profile(request):
    name = request.query_params.get('name')  
    if not name:
        return Response({"error": "Name query parameter is required."}, status=status.HTTP_400_BAD_REQUEST) 
    try:
        customers = Customer.objects.get(name=name)
        serializer = CustomerSerializer(customers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def save_profile(request):
    """
    If profile exists → update; else → create new
    """
    name = request.data.get('name')
    try:
        customer = Customer.objects.get(name=name)
        serializer = CustomerSerializer(customer, data=request.data)
    except Customer.DoesNotExist:
        serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Record saved successfully!'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)