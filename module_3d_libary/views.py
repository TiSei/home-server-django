from django.http import JsonResponse
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse

def standard_weppage_attr(title = None, icon = None, menu = None):
    config = apps.get_app_config(__name__.split('.')[0])
    return {
        'Title':(title if title else config.verbose_name),
        'Favicon':config.favicon,
        'Icon':(icon if icon else config.icon),
        'Menu':(menu if menu else '&quot;/3D_Libary/menu.json&quot;'),
        }

def menu_json(request):
    return JsonResponse({
        '&#8962;':reverse('index'),
        }, safe=True)

def index(request):
    return render(request, '3d_libary/home.html', {
        'Website':standard_weppage_attr(),
        })
