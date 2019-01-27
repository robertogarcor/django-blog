# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django import forms

from ..users.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'inputName',
                                               'class': 'form-control',
                                               'placeholder': 'User Name',
                                               'autofocus': 'True'}),

            'password': forms.PasswordInput(attrs={'id': 'inputPassword',
                                                   'class': 'form-control',
                                                   'placeholder': 'Password'}),
        }


class UserRegisterForm(UserCreationForm):

    error_messages = {
        'username_exists': 'Username already exists. Please enter it again.',
        'password_mismatch': 'The two password fields didn\'''t match.',
        'email_exists': 'This email exists and is active. Please enter it again.',
    }

    username = forms.CharField(max_length="50",
                               widget=forms.TextInput(attrs={
                                   'id': 'inputName',
                                   'class': 'form-control',
                                   'placeholder': 'Enter user name',
                                   }))

    password1 = forms.CharField(max_length="50",
                                widget=forms.PasswordInput(attrs={
                                    'id': 'inputPassword1',
                                    'class': 'form-control',
                                    'placeholder': 'Enter password',
                                    }))

    password2 = forms.CharField(max_length="50",
                                widget=forms.PasswordInput(attrs={
                                    'id': 'inputPassword2',
                                    'class': 'form-control',
                                    'placeholder': 'Repeat password',
                                    }))

    email = forms.CharField(max_length="50",
                            widget=forms.EmailInput(attrs={
                                'id': 'inputEmail',
                                'class': 'form-control',
                                'placeholder': 'Enter email',
                                }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', )
        widgets = {

            'first_name': forms.TextInput(attrs={'id': 'inputFirstName',
                                                 'class': 'form-control',
                                                 'placeholder': 'Enter first name',
                                                 }),

            'last_name': forms.TextInput(attrs={'id': 'inputLastName',
                                                'class': 'form-control',
                                                'placeholder': 'Enter last name',
                                                }),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(self.error_messages['username_exists'])
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'])
        return password2

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages['email_exists'])
        return email

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserEmailChangeForm(forms.Form):

    error_messages = {
        'email_exists': 'This email exists and is active. Please enter it again.',
        'email_mismatch': 'The two email fields didn\'''t match.',
        'password_invalid': 'Your old password was entered incorrectly. Please enter it again.',
    }

    new_email1 = forms.CharField(max_length="50",
                                label="New email",
                                widget=forms.EmailInput(attrs={
                                        'id': 'new_email1',
                                        'placeholder': 'Enter Email',
                                    }))

    new_email2 = forms.CharField(max_length="50",
                                 label="Confirmation email",
                                 widget=forms.EmailInput(attrs={
                                     'id': 'new_email1',
                                     'placeholder': 'Enter Email',
                                 }))

    confirm_password = forms.CharField(max_length="50",
                                       label="Confirmation your password",
                                       widget=forms.PasswordInput(attrs={
                                            'id': 'password',
                                            'placeholder': 'Confirmation Password',
                                        }))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserEmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email2(self):
        new_email1 = self.cleaned_data['new_email1'].lower()
        new_email2 = self.cleaned_data['new_email2'].lower()

        if new_email1 != new_email2:
            raise forms.ValidationError(self.error_messages['email_mismatch'])

        if User.objects.filter(email=new_email2).exists():
            if new_email2 != self.request.user.email:
                raise forms.ValidationError(self.error_messages['email_exists'])

        self.request.user.email = new_email2
        return new_email2

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if not check_password(confirm_password, self.request.user.password):
            raise forms.ValidationError(self.error_messages['password_invalid'])
        return confirm_password


class UserPasswordChangeForm(PasswordChangeForm):
    pass



