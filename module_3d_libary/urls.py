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
]
