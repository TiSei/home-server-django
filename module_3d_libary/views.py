from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.urls import reverse
from .forms import TagForm, TagGroupForm
from .models import Tag, Tag_Group

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
        'Website':standard_weppage_attr(title=title),
        'form': form,
        'object':form.instance,
        'action':path,
        }

def menu_json(request):
    return JsonResponse({
        'Tags':reverse('3d_libary:tag_groups_and_tags'),
        '&#8962;':reverse('index'),
        }, safe=True)

def index(request):
    return render(request, '3d_libary/home.html', {
        'Website':standard_weppage_attr(),
        })

def page_tag_groups_and_tags(request):
    return None

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
            form = form_class(request.POST, instance=instance)
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
    return render(request, '3d_libary/form.html', standard_form_attr(title, form, request.path))

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
