from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from message_board.models import Post
from message_board.serializers import PostSerializer
from message_board.serializers import UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
