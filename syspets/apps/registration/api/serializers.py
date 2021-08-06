# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
    ValidationError,
    )

from apps.adnews.api.serializers import AdnewListSerializer

from apps.users.models import User


class UserRegisterSerializer(ModelSerializer):
    password2 = CharField(label='Confirm password')
    email = EmailField(label='Email')
    email2 = EmailField(label='Confirm email')

    class Meta:
        model = User
        fields = (
                  'username',
                  'password',
                  'password2',
                  'first_name',
                  'last_name',
                  'email',
                  'email2',
                  )
        extra_kwargs = {
            'password': {'write_only': True}, # not include in output object representation 
        }

    def validate(self, data):
        email = data.get('email').lower()
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('This email has already registered.')
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must match.')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password')
        password2 = value
        if password1 != password2:
            raise ValidationError('Passwords must match.')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        
        user = User(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        
        user.set_password(password)
        user.save()
        return validated_data
    
    # Method to modify output object representation
    def to_representation(self, instance):
        # instance is object serializer 
        user = super().to_representation(instance)
        user.pop('password2')
        user.pop('email2')
        return user



class UserLoginSerializer(ModelSerializer):
    username = CharField()
    first_name = CharField(allow_blank=True, read_only=True)
    last_name = CharField(allow_blank=True, read_only=True)
    description = CharField(allow_blank=True, read_only=True)
    image = CharField(allow_blank=True, read_only=True)
    token = CharField(allow_blank=True, read_only=True)

    adnews = AdnewListSerializer(source='adnew_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'description',
            'image',
            'token',
            'adnews',
            )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        username = data.get('username', None)
        password = data['password']
        if not username:
            raise ValidationError('A username is required to login')

        user_qs = User.objects.filter(username=username)

        if not user_qs.exists() and user_qs.count() == 0:
            raise ValidationError('This username is not valid.')

        #user_obj = get_object_or_404(User, username=user_qs.first())
        user_obj = user_qs.first()

        if not user_obj.check_password(password):
            raise ValidationError('Incorrect credentials please try again')

        token, created = Token.objects.get_or_create(user=user_obj)
        #data['token'] = token.key
        user_obj.token = token.key

        return user_obj




