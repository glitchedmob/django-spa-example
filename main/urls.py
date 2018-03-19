from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path, include

from  message_board import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Catch all route
    re_path(r'^.*$', lambda request: render(request, 'base.html')),
]

