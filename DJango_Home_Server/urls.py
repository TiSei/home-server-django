"""
DJango_Home_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from DJango_Home_Server.views.server_views import IndexTemplateView

urlpatterns = [
    path('',IndexTemplateView.as_view(),name='index'),
]

for config in apps.get_app_configs():
    if config.name.startswith('module_'):
        urlpatterns.append(
            path(config.link, include(config.name+'.urls'))
        )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
