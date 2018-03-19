from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path,include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from  message_board import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*$', lambda request: render(request, 'base.html')),
]

