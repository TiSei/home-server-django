from django.shortcuts import render
from django.apps import apps

def standard_weppage_attr(title = None, icon = None):
    config = apps.get_app_config(__name__.split('.')[0])
    return {
        'Title':(title if title else config.verbose_name),
        'Favicon':config.favicon,
        'Icon':(icon if icon else config.icon)
        }

def page_home(request):
    return render(request, '3d_libary/home.html', {
        'Website':standard_weppage_attr(),
        })