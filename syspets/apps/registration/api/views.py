# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
    )

from rest_framework.generics import (
    CreateAPIView,
    )

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )

from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    )

from apps.users.models import User

# Create your views here.


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)





