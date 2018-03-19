from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path,include
from rest_framework import routers

from  message_board import views


urlpatterns = [
    path('api/', include('message_board.urls')),
    path('admin/', admin.site.urls),
    # Catch all route
    re_path(r'^.*$', lambda request: render(request, 'base.html')),
]

