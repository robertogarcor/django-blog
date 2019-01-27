
from django.conf.urls import url, include

from .views import (
                    login,
                    logout,
                    UserRegisterView,
                    UserPasswordChangeView,
                    UserPasswordChangeDoneView,
                    UserEmailChangeDoneView,
                    user_email_change
                    )

urlpatterns = [
    url(r'^signin/$', login, name='signin'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', UserRegisterView.as_view(), name='signup'),
    url(r'^password_change/$', UserPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change_done/$', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^email_change/$', user_email_change, name='email_change'),
    url(r'^email_change_done/$', UserEmailChangeDoneView.as_view(), name='email_change_done'),


]