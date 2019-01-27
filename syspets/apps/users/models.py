# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    description = models.TextField(max_length=512,  blank=True)
    image = models.ImageField(upload_to='images/users', blank=True)








