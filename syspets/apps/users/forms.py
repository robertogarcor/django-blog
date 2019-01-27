# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User


class UserEditForm(UserChangeForm):

    username = forms.CharField(max_length="50",
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter User Name',
                               }))

    # Important! if fields required or declare in widgets -> Default: is not required
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter First name',
                               }))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'description', 'image')
        widgets = {

            'last_name': forms.TextInput(attrs={
                                                'placeholder': 'Enter Last name',
                                                }),

            'description': forms.Textarea(attrs={
                                                 'placeholder': 'Enter Description',
                                                })

        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name is None or first_name == "":
            raise forms.ValidationError('This fields is required')
        return first_name















