
from django.conf.urls import url, include

from .views import (
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    )

app_name = 'users'


urlpatterns = [
    url(r'^$', UserListAPIView.as_view(), name='user-list'),
    url(r'^user/(?P<pk>\d+)/$', UserRetrieveAPIView.as_view(), name='user-detail'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateAPIView.as_view(), name='user-update'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteAPIView.as_view(), name='user-delete'),

]

