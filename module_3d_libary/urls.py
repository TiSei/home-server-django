from django.urls import path
from module_3d_libary.views.form_views import (
    PartActionView,
    PrintProfilActionView,
    ProjectActionView,
    TagActionView,
    TagGroupActionView,
    VariantActionView
)
from module_3d_libary.views.template_views import (
    PartTemplateView,
    PrintProfilTemplateView,
    ProjectTemplateView,
    SinglePartTemplateView,
    SingleProjectTemplateView,
    TagAndTagGroupTemplateView,
    TemplateView_3d_libary,
    VariantTemplateView,
    menu)

app_name = '3d_libary'

urlpatterns = [
    path('',TemplateView_3d_libary.as_view(
        template_name='3d_libary/index.html'
    ),name='index'),
    path('menu.json',menu,name='menu'),
    # tags
    path('tags/',TagAndTagGroupTemplateView.as_view(),name='tag_groups_and_tags'),
    path('tags/action/',TagActionView.as_view(),name='tag_new'),
    path('tags/action/<int:pk>',TagActionView.as_view(),name='tag_action'),
    # tag groups
    path('tag_groups/',TagAndTagGroupTemplateView.as_view(),name='tag_groups_and_tags'),
    path('tag_groups/action/',TagGroupActionView.as_view(),name='tag_group_new'),
    path('tag_groups/action/<int:pk>',TagGroupActionView.as_view(),name='tag_group_action'),
    # print profils
    path('print_profils/',PrintProfilTemplateView.as_view(),name='print_profils'),
    path('print_profils/action/',PrintProfilActionView.as_view(),name='print_profil_new'),
    path('print_profils/action/<int:pk>',PrintProfilActionView.as_view(),name='print_profil_action'),
    # projects
    path('projects/',ProjectTemplateView.as_view(),name='projects'),
    path('projects/action/',ProjectActionView.as_view(),name='project_new'),
    path('projects/action/<int:pk>',ProjectActionView.as_view(),name='project_action'),
    path('projects/<int:pk>',SingleProjectTemplateView.as_view(),name="project_single"),
    # parts
    path('parts/',PartTemplateView.as_view(),name='parts'),
    path('parts/action/',PartActionView.as_view(),name='part_new'),
    path('parts/action/<int:pk>',PartActionView.as_view(),name='part_action'),
    path('parts/<int:pk>',SinglePartTemplateView.as_view(),name="part_single"),
    # variants
    path('variants/',VariantTemplateView.as_view(),name='variants'),
    path('variants/action/',VariantActionView.as_view(),name='variant_new'),
    path('variants/action/<int:pk>',VariantActionView.as_view(),name='variant_action'),
]
