from django.http import JsonResponse
from django.urls import reverse
from django.apps import apps
from views.TemplateView import StandardTemplateView

def get_3d_libary_weppage_attr():
    config = apps.get_app_config(__name__.split('.')[0])
    return {
        'Title':config.verbose_name,
        'Favicon':config.favicon,
        'Icon':config.icon,
        'Menu':'&quot;/3D_Libary/menu.json&quot;',
    }

def menu(request):
    return JsonResponse({
        'Projekte':reverse('3d_libary:projects'),
        'Projektteile':reverse('3d_libary:parts'),
        'Bauteile':reverse('3d_libary:variants'),
        'Tags':reverse('3d_libary:tag_groups_and_tags'),
        'Druckprofile':reverse('3d_libary:print_profils'),
        '&#8962;':reverse('index'),
        }, safe=True)

class TemplateView_3d_libary(StandardTemplateView):
    webpage_attr = get_3d_libary_weppage_attr()
