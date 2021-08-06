# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    )

from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    )

from .serializers import (
    AdnewListSerializer,
    AdnewRetrieveSerializer,
    AdnewCreateSerializer,
    AdnewUpdateSerializer,
    AdnewDeleteSerializer,
    CommentListSerializer,
    CommentRetrieveSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
    CommentDeleteSerializer,
    )

from ..models import Adnew, Comment

# Create your views here.

# Adnews #


class AdnewListAPIView(ListAPIView):
    queryset = Adnew.objects.all()
    serializer_class = AdnewListSerializer


class AdnewRetrieveAPIView(RetrieveAPIView):
    queryset = Adnew.objects.all()
    serializer_class = AdnewRetrieveSerializer


class AdnewCreateAPIView(CreateAPIView):
    queryset = Adnew.objects.all()  # It is not necessary
    serializer_class = AdnewCreateSerializer


class AdnewUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Adnew.objects.all()
    serializer_class = AdnewUpdateSerializer


class AdnewDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Adnew.objects.all()
    serializer_class = AdnewDeleteSerializer


# Comments #


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()  # It is not necessary
    serializer_class = CommentCreateSerializer


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer


class CommentDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer



