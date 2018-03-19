from django.urls import path, include

from message_board import views

urlpatterns = [
    path('', include(router.urls)),
]
