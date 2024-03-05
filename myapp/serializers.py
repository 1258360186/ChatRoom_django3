from rest_framework import serializers
from myapp.models import Userinfo

class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userinfo
        fields = ['nickname', 'headImg']

