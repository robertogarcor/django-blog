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

from .views import UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [

    url(r'^user/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^user/(?P<slug>[-\w]+)/update/$', UserUpdateView.as_view(), name='user_update_form'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='user_delete'),
    url(r'^user/(?P<slug>[-\w]+)/delete/$', UserDeleteView.as_view(), name='user_delete'),

]


