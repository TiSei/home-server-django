from django.urls import path
from . import views

app_name = '3d_libary'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu.json',views.menu_json,name='menu'),
]
