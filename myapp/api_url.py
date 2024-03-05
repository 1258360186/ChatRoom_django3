from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = [
    path('', views.first_api),
    path('login/', views.LoginView.as_view()),
]