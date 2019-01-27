# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined')

    fieldsets = (
        ('User', {'fields': ('username',
                             'password'
                             )}),

        ('Personal Info', {'fields': ('first_name',
                                      'last_name',
                                      'email',
                                      'description',
                                      'image',
                                      )}),

        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions'
                                    )}),

        ('Important Dates', {'fields': ('last_login',
                                        'date_joined'
                                        )}),
    )


admin.site.register(User, UserAdmin)

