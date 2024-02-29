from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def first_api(request):
    return Response({'message': 'Hello World!'})


@api_view(['POST'])
def login_api(request):
    name = request.data.get("name")
    password = request.data.get("password")
    user = User.objects.filter(username=name).first()
    if not user:
        return Response({'state': False,'message': '用户不存在'})
    check = check_password(password, user.password)
    if not check:
        return Response({'state': False, 'message': '密码不正确'})
    token = Token.objects.update_or_create(user=user)
    token = Token.objects.get(user=user).key
    return Response({'state': True,'token' : token })