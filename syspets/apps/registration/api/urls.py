
from django.conf.urls import url, include

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserLogoutView,
    )

app_name = 'registration'


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^logout/$', UserLogoutView.as_view(), name='logout'),

]

