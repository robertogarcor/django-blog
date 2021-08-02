# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import AdnewForm, CommentForm
from .models import Adnew, Comment


# Create your views here.


class AdnewListView(LoginRequiredMixin, ListView):
    model = Adnew  # Equals: queryset = Adnew.objects.all()
    template_name = 'adnews/adnew_list.html'  # Default: <app_label>/<model_name>_list.html
    queryset = Adnew.objects.all().order_by('-created')  # Default: Model.objects.all()
    paginate_by = 5  # if pagination is desired
    context_object_name = 'adnews_list'  # Default: object_list

    def get_context_data(self, **kwargs):
        context = super(AdnewListView, self).get_context_data(**kwargs)
        number_comments = [Comment.objects.filter(adnew=adnew).count() for adnew in context['object_list']]
        context['adnews_comments'] = zip(context['object_list'], number_comments)
        return context


class AdnewCreateView(LoginRequiredMixin, CreateView):
    model = Adnew
    form_class = AdnewForm
    template_name = 'adnews/adnew_form.html'  # Default: <app_label>/<model_name>_form.html

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user})

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.user = self.request.user
            return super(AdnewCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(AdnewCreateView, self).form_invalid(form)


class AdnewDetailView(LoginRequiredMixin, DetailView):
    model = Adnew
    template_name = 'adnews/adnew_detail.html'  # Default: <app_label>/<model_name>_detail.html
    context_object_name = 'adnew'  # Default: object

    def get_context_data(self, **kwargs):
        context = super(AdnewDetailView, self).get_context_data(**kwargs)
        comments_list = Comment.objects.filter(adnew=context['object']).order_by('-created')
        number_comments = Comment.objects.filter(adnew=context['object']).count()
        context['adnew_comments'] = comments_list
        context['number_comments'] = number_comments
        return context


class AdnewUptadeView(LoginRequiredMixin, UpdateView):
    model = Adnew
    form_class = AdnewForm
    template_name = 'adnews/adnew_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(AdnewUptadeView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(AdnewUptadeView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user, })


class AdnewDeleteView(LoginRequiredMixin, DeleteView):
    model = Adnew
    template_name = 'adnews/adnew_confirm_delete.html'  # Default: <app_label>/<model_name>_confirm_delete.html
    context_object_name = 'adnew'  # Default: object

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'slug': self.object.user, })


# COMMENTS #

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'adnews/comment_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.user = self.request.user
            #adnew_obj = get_object_or_404(Adnew, pk=self.kwargs['pk'])
            adnew_obj = Adnew.objects.get(pk=self.kwargs['pk'])
            form.instance.adnew = adnew_obj
            return super(CommentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(CommentCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('adnews:adnew_detail', kwargs={'pk': self.object.adnew_id})
        #return reverse('users:user_detail', kwargs={'slug': self.object.user})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'adnews/comment_confirm_delete.html'  # Default: <app_label>/<model_name>_confirm_delete.html
    context_object_name = 'comment'  # Default: object

    def get_success_url(self):
        return reverse('adnews:adnew_detail', kwargs={'pk': self.object.adnew.id, })


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'adnews/comment_form.html'  # Default: <app_label>/<model_name>_form.html

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(CommentUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.method == 'POST':
            return super(CommentUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('adnews:adnew_detail', kwargs={'pk': self.object.adnew.id, })

