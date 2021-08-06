"""syspets URL Configuration

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

    #url(r'^user/$', user, {'template_name':'user/user.html'}, name='user'),
    #url(r'^login/$', login, name='login'),
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

from .views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='homepage'),
    url(r'^accounts/', include('apps.registration.urls', namespace='accounts')),
    url(r'^adnews/', include('apps.adnews.urls', namespace='adnews')),
    url(r'^users/', include('apps.users.urls', namespace='users')),

    url(r'^api/1.0/accounts/', include('apps.registration.api.urls', namespace='api-accounts')),
    url(r'^api/1.0/users/', include('apps.users.api.urls', namespace='api-users')),
    url(r'^api/1.0/adnews/', include('apps.adnews.api.urls', namespace='api-adnews')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


