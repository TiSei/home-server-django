from django.http import JsonResponse
from django.urls import reverse
from django.apps import apps
from views.FormView import StandardFormView
from views.TemplateListView import StandardTemplateListView
from views.TemplateSingleView import StandardTemplateSingleView
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
    styles = ['/static/css/3d_libary_style.css']
    def get_webpage_attr(self):
        return get_3d_libary_weppage_attr(True)

class TemplateListView_3d_libary(TemplateView_3d_libary, StandardTemplateListView):
    pass

class TemplateSingleView_3d_libary(TemplateView_3d_libary, StandardTemplateSingleView):
    pass

class PrintProfilTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
        return [
            StandardTemplateListView.build_config(
                'Druckprofile',
                '3d_libary:print_profil_new',
                self.get_all(Print_Profil),
                '3d_libary/_print_profil.html',
                page_size=10)]

class TagAndTagGroupTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
        return [
            StandardTemplateListView.build_config(
                'Tag-Gruppen',
                '3d_libary:tag_group_new',
                self.get_all(Tag_Group),
                '3d_libary/_tag_group.html',
                two_cols=False,
                action_url='3d_libary:tag_group_action'),
            StandardTemplateListView.build_config(
                'Tags',
                '3d_libary:tag_new',
                self.get_all(Tag),
                '3d_libary/_tag.html',
                two_cols=False,
                action_url='3d_libary:tag_action')]

class ProjectTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
        return [
            StandardTemplateListView.build_config(
                'Projekte',
                '3d_libary:project_new',
                self.get_all(Project),
                '3d_libary/_project.html',
                has_filter=True,
                page_size=10)]
    def apply_filter(self, queryset):
        tag_set = set(map(int,self.request.GET.getlist('tags')))
        filtered_projects = [p for p in queryset if tag_set.issubset(set(t.pk for t in p.get_all_tags()))]
        return filtered_projects, '3d_libary/filter_project.html', {'title':'Filter','tags':self.get_all(Tag),'current_tags':tag_set}

class PartTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
        return [
            StandardTemplateListView.build_config(
                'Projektteile',
                '3d_libary:part_new',
                self.get_all(Part),
                '3d_libary/_part.html',
                page_size=10)]

class PartTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
        return [
            StandardTemplateListView.build_config(
                'Projektteile',
                '3d_libary:part_new',
                self.get_all(Part),
                '3d_libary/_part.html',
                page_size=10)]

class VariantTemplateView(TemplateListView_3d_libary):
    def get_configs(self):
         return [
             StandardTemplateListView.build_config(
                'Bauteile',
                '3d_libary:variant_new',
                self.get_all(Variant),
                '3d_libary/_variant.html',
                page_size=10)]

class SingleProjectTemplateView(TemplateSingleView_3d_libary):
    def get_config(self, pk):
        project = self.get_instance(Project, pk)
        return StandardTemplateSingleView.build_config(
            'Projekt',
            project.name,
            project,
            '3d_libary:project_action',
            [StandardTemplateSingleView.build_paragraph(
                 'Projektziel',project.target
                 )],
            [StandardTemplateSingleView.build_details(
                 'Projektteile','3d_libary:part_new',project.parts.all(),'3d_libary/_part.html'
                 ),
             StandardTemplateSingleView.build_details(
                 'Bauteile','3d_libary:variant_new',project.get_all_variants(),'3d_libary/_variant.html'
                 )]
            )

class SinglePartTemplateView(TemplateSingleView_3d_libary):
    def get_config(self, pk):
        part = self.get_instance(Part, pk)
        return StandardTemplateSingleView.build_config(
            'Teilprojekt',
            part.name,
            part,
            '3d_libary:part_action',
            [StandardTemplateSingleView.build_paragraph(
                 'Beschreibung',part.desc
                 ),
             StandardTemplateSingleView.build_paragraph(
                 'Projekt',part.project.name,instance=part.project,detail_url='3d_libary:project_single'
                 )],
            [StandardTemplateSingleView.build_details(
                 'Bauteile','3d_libary:variant_new',part.variants.all(),'3d_libary/_variant.html'
                 )]
            )
