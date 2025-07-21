from django.shortcuts import render
from django.apps import apps

def standard_webpage_attr():
    return {
        'Title':'Home Server',
        'Favicon':'Home_Server_Icon.png',
        'Icon':'Home_Server.png',
        }

def page_home(request):
    api_list = []
    for config in apps.get_app_configs():
        if config.name.startswith('module_'):
            api_list.append({
                'Name':config.verbose_name,
                'Link':config.link,
                'IconPath':config.icon,
            })
    return render(request, 'home.html', {
        'Website':standard_webpage_attr,
        'APIs': api_list,
        })
