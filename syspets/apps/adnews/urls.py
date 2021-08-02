"""
syspets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from .views import AdnewListView
from .views import AdnewCreateView, AdnewDetailView, AdnewUptadeView, AdnewDeleteView
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView

app_name = 'adnews'

urlpatterns = [
    url(r'^$', AdnewListView.as_view(), name='adnew_list'),
    url(r'^adnew/add/$', AdnewCreateView.as_view(), name='adnew_add'),
    url(r'^adnew/(?P<pk>\d+)/$', AdnewDetailView.as_view(), name='adnew_detail'),
    url(r'^adnew/(?P<pk>\d+)/update/$', AdnewUptadeView.as_view(), name='adnew_update_form'),
    url(r'^adnew/(?P<pk>\d+)/delete/$', AdnewDeleteView.as_view(), name='adnew_delete'),
    url(r'^adnew/(?P<pk>\d+)/comment/add/$', CommentCreateView.as_view(), name='comment_add'),
    url(r'^comments/(?P<pk>\d+)/delete/$', CommentDeleteView.as_view(), name='comment_delete'),
    url(r'^comments/(?P<pk>\d+)/update/$', CommentUpdateView.as_view(), name='comment_update_form'),

]
