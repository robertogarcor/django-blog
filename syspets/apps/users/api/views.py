# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    )

from .serializers import (
    UserListSerializer,
    UserRetrieveSerializer,
    UserUpdateSerializer,
    UserDeleteSerializer
    )

from ..models import User

# Create your views here.


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteAPIView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer




