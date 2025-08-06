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
        attrs['Menu'] = '&quot;/3D_Libary/menu.json&quot;'
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
        self.data_context['tags'] = self.get_all(Tag)
        self.data_context['tag_groups'] = self.get_all(Tag_Group)
        return super().get_context_data(**kwargs)

class PrintProfilTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/print_profils.html'
    def get_context_data(self, **kwargs):
        self.data_context['print_profils'] = self.get_all(Print_Profil)
        return super().get_context_data(**kwargs)

class ProjectTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/projects.html'
    def get_context_data(self, **kwargs):
        self.data_context['projects'] = self.get_all(Project)
        return super().get_context_data(**kwargs)

class PartTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/parts.html'
    def get_context_data(self, **kwargs):
        self.data_context['parts'] = self.get_all(Part)
        return super().get_context_data(**kwargs)

class VariantTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/variants.html'
    def get_context_data(self, **kwargs):
        self.data_context['variants'] = self.get_all(Variant)
        return super().get_context_data(**kwargs)

class SingleProjectTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/single_project.html'
    def get_context_data(self, **kwargs):
        project_id = self.kwargs.get('pk')
        self.data_context['project'] = self.get_instance(Project, project_id)
        return super().get_context_data(**kwargs)

class SinglePartTemplateView(TemplateView_3d_libary):
    template_name='3d_libary/single_part.html'
    def get_context_data(self, **kwargs):
        part_id = self.kwargs.get('pk')
        self.data_context['part'] = self.get_instance(Part, part_id)
        return super().get_context_data(**kwargs)
