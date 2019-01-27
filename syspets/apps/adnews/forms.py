# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Adnew, Comment


class AdnewForm(forms.ModelForm):

    class Meta:
        model = Adnew
        fields = ('title', 'description', 'image')

        widgets = {
            'title': forms.TextInput(attrs={
                                            'placeholder': 'Enter title adnew',
                                            }),

            'description': forms.Textarea(attrs={
                                                 'placeholder': 'Enter description',
                                                 }),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('description', )

        widgets = {
            'description': forms.Textarea(attrs={
                                                 'placeholder': 'Enter comment',
                                                 }),
        }






