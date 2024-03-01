from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Userinfo(models.Model):

    nickname = models.CharField(max_length=200,blank=True,null=True)
    headImg = models.ImageField(upload_to='headImg/',blank=True,null=True)
    belong = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userinfo_user',blank=True,null=True)
    def __int__(self):
        return self.id
