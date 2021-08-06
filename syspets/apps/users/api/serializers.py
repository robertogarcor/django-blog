# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.adnews.api.serializers import (
    AdnewListSerializer,
    )

from ..models import User


class UserListSerializer(serializers.ModelSerializer):

    adnews = AdnewListSerializer(source="adnew_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'adnews',
                  )


class UserRetrieveSerializer(serializers.ModelSerializer):

    adnews = AdnewListSerializer(source="adnew_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'adnews',
                  )


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  )


class UserDeleteSerializer(serializers.ModelSerializer):

    adnews = AdnewListSerializer(source="adnew_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'description',
                  'image',
                  'adnews',
                  )



