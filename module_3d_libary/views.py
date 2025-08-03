from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.urls import reverse
from .forms import VariantForm, PartForm, ProjectForm, PrintProfilForm, TagForm, TagGroupForm
from .models import Variant, Part, Project, Print_Profil, Tag, Tag_Group

def standard_weppage_attr(title = None, icon = None, menu = None):
    config = apps.get_app_config(__name__.split('.')[0])
    return {
        'Title':(title if title else config.verbose_name),
        'Favicon':config.favicon,
        'Icon':(icon if icon else config.icon),
        'Menu':(menu if menu else '&quot;/3D_Libary/menu.json&quot;'),
        }

def standard_form_attr(title, form, path):
    return {
        'Website':standard_weppage_attr(),
        'form':{
            'innerBody':form,
            'action':path,
            'title':title,
            }
        }

def menu_json(request):
    return JsonResponse({
        'Projekte':reverse('3d_libary:projects'),
        'Projektteile':reverse('3d_libary:parts'),
        'Bauteile':reverse('3d_libary:variants'),
        'Tags':reverse('3d_libary:tag_groups_and_tags'),
        'Druckprofile':reverse('3d_libary:print_profils'),
        '&#8962;':reverse('index'),
        }, safe=True)

def index(request):
    return render(request, '3d_libary/index.html', {
        'Website':standard_weppage_attr(),
        })

def page_tag_groups_and_tags(request):
    return render(request, '3d_libary/tag_groups_and_tags.html', {
        'Website':standard_weppage_attr(),
        'tags':Tag.objects.all(),
        'tag_groups':Tag_Group.objects.all(),
        })

def page_print_profils(request):
    return render(request, '3d_libary/print_profils.html', {
        'Website':standard_weppage_attr(),
        'print_profils':Print_Profil.objects.all(),
        })

def page_projects(request):
    return render(request, '3d_libary/projects.html', {
        'Website':standard_weppage_attr(),
        'projects':Project.objects.all(),
        })

def page_parts(request):
    return render(request, '3d_libary/parts.html', {
        'Website':standard_weppage_attr(),
        'parts':Part.objects.all().order_by('project'),
        })

def page_variants(request):
    return render(request, '3d_libary/variants.html', {
        'Website':standard_weppage_attr(),
        'variants':Variant.objects.all().order_by('part'),
        })

def handle_action_request(
    request,
    model_class,
    form_class,
    pk=None,
    title_prefix='Element',
    redirect_post='',
    redirect_delete='',
):
    instance = get_object_or_404(model_class, pk=pk) if pk else None

    if request.method == 'POST':
        method = request.POST.get('_method', '').upper()
        if method == 'POST':
            form = form_class(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect(redirect_post)
        elif method == 'DELETE':
            if instance:
                instance.delete()
                return redirect(redirect_delete)
    else:
        form = form_class(instance=instance)

    title = f"{title_prefix} bearbeiten" if instance else f"Neuen {title_prefix} speichern"
    return render(request, 'standard_form_layout.html', standard_form_attr(title, form, request.path))

def action_tag(request, pk=None):
    return handle_action_request(
        request,
        model_class=Tag,
        form_class=TagForm,
        pk=pk,
        title_prefix='Tag',
        redirect_post=reverse('3d_libary:tag_groups_and_tags'),
        redirect_delete=reverse('3d_libary:tag_groups_and_tags'),
    )

def action_tag_group(request, pk=None):
    return handle_action_request(
        request,
        model_class=Tag_Group,
        form_class=TagGroupForm,
        pk=pk,
        title_prefix='Tag-Gruppe',
        redirect_post=reverse('3d_libary:tag_groups_and_tags'),
        redirect_delete=reverse('3d_libary:tag_groups_and_tags'),
    )

def action_print_profil(request, pk=None):
    return handle_action_request(
        request,
        model_class=Print_Profil,
        form_class=PrintProfilForm,
        pk=pk,
        title_prefix='Druckprofil',
        redirect_post=reverse('3d_libary:print_profils'),
        redirect_delete=reverse('3d_libary:print_profils'),
    )

def action_project(request, pk=None):
    return handle_action_request(
        request,
        model_class=Project,
        form_class=ProjectForm,
        pk=pk,
        title_prefix='Projekt',
        redirect_post=reverse('3d_libary:projects'),
        redirect_delete=reverse('3d_libary:projects'),
    )

def action_part(request, pk=None):
    return handle_action_request(
        request,
        model_class=Part,
        form_class=PartForm,
        pk=pk,
        title_prefix='Projektteil',
        redirect_post=reverse('3d_libary:parts'),
        redirect_delete=reverse('3d_libary:parts'),
    )

def action_variant(request, pk=None):
    return handle_action_request(
        request,
        model_class=Variant,
        form_class=VariantForm,
        pk=pk,
        title_prefix='Bauteil',
        redirect_post=reverse('3d_libary:variants'),
        redirect_delete=reverse('3d_libary:variants'),
    )