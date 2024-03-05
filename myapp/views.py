import base64

import cv2
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from myapp.models import Userinfo
from django.conf import settings
from myapp.serializers import UserinfoSerializer
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
    image_path = Userinfo.objects.get(belong=user).headImg.url #r'D:\Code\ChatRoom_django3\upload\test.jpg'  # 替换为你的图片路径
    image_path = str(settings.BASE_DIR) + image_path.replace('/', '\\')
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        # 图像加载失败
        print("Failed to load image")
    _, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer).decode()
    return Response({'state': True,'token' : token ,'image':img_str})



class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request, format=None):
        name = request.data.get("name")
        password = request.data.get("password")
        user = User.objects.filter(username=name).first()
        if not user:
            return Response({'state': False, 'message': '用户不存在'})
        check = check_password(password, user.password)
        if not check:
            return Response({'state': False, 'message': '密码不正确'})
        token = Token.objects.update_or_create(user=user)
        token = Token.objects.get(user=user).key
        image_path = Userinfo.objects.get(
            belong=user).headImg.url  # r'D:\Code\ChatRoom_django3\upload\test.jpg'  # 替换为你的图片路径
        image_path = str(settings.BASE_DIR) + image_path.replace('/', '\\')
        print(image_path)
        image = cv2.imread(image_path)
        if image is None:
            # 图像加载失败
            print("Failed to load image")
        _, buffer = cv2.imencode('.jpg', image)
        img_str = base64.b64encode(buffer).decode()
        return Response({'state': True, 'token': token, 'image': img_str})