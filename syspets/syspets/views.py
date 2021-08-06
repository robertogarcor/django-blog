# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from apps.adnews.models import Adnew

from datetime import date, datetime

# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    queryset = Adnew.objects.all().order_by('-created')[:3]
    context_object_name = 'adnews_list'  # Default: object_list

    def dateYear():
        today = date.today()
        return today.year
