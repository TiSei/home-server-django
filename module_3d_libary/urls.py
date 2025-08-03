from django.urls import path
from . import views

app_name = '3d_libary'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu.json',views.menu_json,name='menu'),
    # tags
    path('tags/',views.page_tag_groups_and_tags,name='tag_groups_and_tags'),
    path('tags/action/',views.action_tag,name='tag_new'),
    path('tags/action/<int:pk>',views.action_tag,name='tag_action'),
    # tag groups
    path('tag_groups/',views.page_tag_groups_and_tags,name='tag_groups_and_tags'),
    path('tag_groups/action/',views.action_tag_group,name='tag_group_new'),
    path('tag_groups/action/<int:pk>',views.action_tag_group,name='tag_group_action'),
    # print profils
    path('print_profils/',views.page_print_profils,name='print_profils'),
    path('print_profils/action/',views.action_print_profil,name='print_profil_new'),
    path('print_profils/action/<int:pk>',views.action_print_profil,name='print_profil_action'),
    # projects
    path('projects/',views.page_projects,name='projects'),
    path('projects/action/',views.action_project,name='project_new'),
    path('projects/action/<int:pk>',views.action_project,name='project_action'),
    # parts
    path('parts/',views.page_parts,name='parts'),
    path('parts/action/',views.action_part,name='part_new'),
    path('parts/action/<int:pk>',views.action_part,name='part_action'),
    # variants
    path('variants/',views.page_variants,name='variants'),
    path('variants/action/',views.action_variant,name='variant_new'),
    path('variants/action/<int:pk>',views.action_variant,name='variant_action'),
]
