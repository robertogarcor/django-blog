# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from ..models import Adnew, Comment

# Comment #


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'adnew',
                  )


class CommentRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'adnew',
                  )


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'adnew',
                  )


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'adnew',
                  )


class CommentDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',
                  'description',
                  'user',
                  'adnew',
                  )


# Adnews #

class AdnewListSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Adnew
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'image',
                  'comments',
                  )


class AdnewRetrieveSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Adnew
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  'image',
                  'comments',
                  )


class AdnewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adnew
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  )


class AdnewUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adnew
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  )


class AdnewDeleteSerializer(serializers.ModelSerializer):

    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Adnew
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'user',
                  'comments',
                  )




