from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def first_api(request):
    return Response({'message': 'Hello World!'})


@api_view(['POST'])
def login_api(request):
    return Response({'state': True})