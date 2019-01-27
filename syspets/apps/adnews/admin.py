# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Adnew, Comment

# Register your models here.


class AdnewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'modified',)
    search_fields = ('title', 'user__username',)
    ordering = ('-created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('adnew', 'user', 'created', 'modified',)
    search_fields = ('adnew__title', 'user__username', 'created', 'description')
    ordering = ('-created',)


admin.site.register(Adnew, AdnewAdmin)
admin.site.register(Comment, CommentAdmin)
