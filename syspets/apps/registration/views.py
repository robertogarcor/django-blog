# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.forms import PasswordChangeForm

from .forms import (LoginForm,
                    UserRegisterForm,
                    UserPasswordChangeForm,
                    UserEmailChangeForm,
                    )

from ..users.models import User

# Create your views here.


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/signup.html'  # Default: <app_label>/<model_name>_form.html
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(UserRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(UserRegisterView, self).form_invalid(form)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/cpassword_change_form.html'  # Default: <app_label>/password_change_form.html
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(UserPasswordChangeView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(UserPasswordChangeView, self).form_invalid(form)


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/cpassword_change_done.html'  # Default: <app_label>/password_change_done.html.html


def user_email_change(request):
    if request.method == 'POST':
        form = UserEmailChangeForm(request.POST, request=request)
        if form.is_valid():
            request.user.save()
            return HttpResponseRedirect(reverse_lazy('accounts:email_change_done'))
    else:
        form = UserEmailChangeForm()
    return render(request, 'registration/email_change_form.html', {'form': form})


class UserEmailChangeDoneView(TemplateView):
    template_name = 'registration/email_change_done.html'


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            # Redirect to a success page.
            # reverse allow encode la url
            return HttpResponseRedirect(reverse_lazy('adnews:adnew_list'))
        else:
            # Return an 'invalid user' error message.
            messages.error(request, 'Username or Password Invalid!')
            return render(request, 'registration/signin.html', {'form': LoginForm()})
    else:
        return render(request, 'registration/signin.html', {'form': LoginForm()})


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout Account Ok.')
    # Redirect encapsulate HttpResponseRedirect, more flexible accept: model,view o url
    return redirect('homepage')












