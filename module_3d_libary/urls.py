from django.urls import path
from module_3d_libary.views.form_views import (
    PartActionView,
    PrintProfilActionView,
    ProjectActionView,
    TagActionView,
    TagGroupActionView,
    VariantActionView
)
from module_3d_libary.views.template_views import (TemplateView_3d_libary, menu)
from .models import (Tag, Tag_Group, Print_Profil, Project, Part, Variant)

app_name = '3d_libary'

urlpatterns = [
    path('',TemplateView_3d_libary.as_view(
        template_name='3d_libary/index.html'
    ),name='index'),
    path('menu.json',menu,name='menu'),
    # tags
    path('tags/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/tag_groups_and_tags.html',
        data_context={'tags': Tag.objects.all(),'tag_groups': Tag_Group.objects.all()}
    ),name='tag_groups_and_tags'),
    path('tags/action/',TagActionView.as_view(),name='tag_new'),
    path('tags/action/<int:pk>',TagActionView.as_view(),name='tag_action'),
    # tag groups
    path('tag_groups/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/tag_groups_and_tags.html',
        data_context={'tags': Tag.objects.all(),'tag_groups': Tag_Group.objects.all()}
    ),name='tag_groups_and_tags'),
    path('tag_groups/action/',TagGroupActionView.as_view(),name='tag_group_new'),
    path('tag_groups/action/<int:pk>',TagGroupActionView.as_view(),name='tag_group_action'),
    # print profils
    path('print_profils/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/print_profils.html',
        data_context={'print_profils': Print_Profil.objects.all()}
    ),name='print_profils'),
    path('print_profils/action/',PrintProfilActionView.as_view(),name='print_profil_new'),
    path('print_profils/action/<int:pk>',PrintProfilActionView.as_view(),name='print_profil_action'),
    # projects
    path('projects/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/projects.html',
        data_context={'projects': Project.objects.all()}
    ),name='projects'),
    path('projects/action/',ProjectActionView.as_view(),name='project_new'),
    path('projects/action/<int:pk>',ProjectActionView.as_view(),name='project_action'),
    # parts
    path('parts/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/parts.html',
        data_context={'parts': Part.objects.all().order_by('project')}
    ),name='parts'),
    path('parts/action/',PartActionView.as_view(),name='part_new'),
    path('parts/action/<int:pk>',PartActionView.as_view(),name='part_action'),
    # variants
    path('variants/',TemplateView_3d_libary.as_view(
        template_name='3d_libary/variants.html',
        data_context={'variants': Variant.objects.all().order_by('part')}
    ),name='variants'),
    path('variants/action/',VariantActionView.as_view(),name='variant_new'),
    path('variants/action/<int:pk>',VariantActionView.as_view(),name='variant_action'),
]
