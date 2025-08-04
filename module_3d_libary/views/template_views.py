from django.http import JsonResponse
from django.urls import reverse
from django.apps import apps
from views.TemplateView import StandardTemplateView
from ..models import (Tag, Tag_Group, Print_Profil, Project, Part, Variant)

def get_3d_libary_weppage_attr(menu = True):
    config = apps.get_app_config(__name__.split('.')[0])
    attrs = {
        'Title': config.verbose_name,
        'Favicon': config.favicon,
        'Icon': config.icon,
    }
    if menu:
        attrs['Menu'] = '"/3D_Libary/menu.json"'
    return attrs

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

class TagAndTagGroupTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/tag_groups_and_tags.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['tag_groups'] = Tag_Group.objects.all()
        return context

class PrintProfilTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/print_profils.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['print_profils'] = Print_Profil.objects.all()
        return context

class ProjectTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/projects.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class PartTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/parts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Part.objects.all()
        return context

class VariantTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/variants.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = Variant.objects.all()
        return context
