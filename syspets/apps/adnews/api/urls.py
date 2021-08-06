
from django.conf.urls import url, include

from .views import (
    AdnewListAPIView,
    AdnewRetrieveAPIView,
    AdnewCreateAPIView,
    AdnewUpdateAPIView,
    AdnewDeleteAPIView,
    CommentListAPIView,
    CommentRetrieveAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
    )

app_name = 'adnews'

urlpatterns = [
    url(r'^$', AdnewListAPIView.as_view(), name='adnew-list'),
    url(r'^adnew/add/$', AdnewCreateAPIView.as_view(), name='adnew-add'),
    url(r'^adnew/(?P<pk>\d+)/$', AdnewRetrieveAPIView.as_view(), name='adnew-detail'),
    url(r'^adnew/(?P<pk>\d+)/update/$', AdnewUpdateAPIView.as_view(), name='adnew-update'),
    url(r'^adnew/(?P<pk>\d+)/delete/$', AdnewDeleteAPIView.as_view(), name='adnew-delete'),
    url(r'^comment/$', CommentListAPIView.as_view(), name='comment-list'),
    url(r'^comment/(?P<pk>\d+)/$', CommentRetrieveAPIView.as_view(), name='comment-detail'),
    url(r'^adnew/(?P<pk>\d+)/comment/add/$', CommentCreateAPIView.as_view(), name='comment_add'),
    url(r'^comment/(?P<pk>\d+)/update/$', CommentUpdateAPIView.as_view(), name='comment-update'),
    url(r'^comment/(?P<pk>\d+)/delete/$', CommentDeleteAPIView.as_view(), name='comment-delete'),

]

