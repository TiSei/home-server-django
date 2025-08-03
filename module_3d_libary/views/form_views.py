from django.urls import reverse_lazy
from views.FormView import StandardFormView
from .template_views import get_3d_libary_weppage_attr
from ..forms import TagForm, TagGroupForm, ProjectForm, PartForm, VariantForm, PrintProfilForm
from ..models import Tag, Tag_Group, Project, Part, Variant, Print_Profil

class FormView_3d_libary(StandardFormView):
    webpage_attr = get_3d_libary_weppage_attr()
    
class TagActionView(FormView_3d_libary):
    model = Tag
    form_class = TagForm
    title_prefix = "Tag"
    success_url = reverse_lazy('3d_libary:tag_groups_and_tags')

class TagGroupActionView(FormView_3d_libary):
    model = Tag_Group
    form_class = TagGroupForm
    title_prefix = "Tag-Gruppe"
    success_url = reverse_lazy('3d_libary:tag_groups_and_tags')

class PrintProfilActionView(FormView_3d_libary):
    model = Print_Profil
    form_class = PrintProfilForm
    title_prefix = "Druckprofil"
    success_url = reverse_lazy('3d_libary:print_profils')

class ProjectActionView(FormView_3d_libary):
    model = Project
    form_class = ProjectForm
    title_prefix = "Projekt"
    success_url = reverse_lazy('3d_libary:projects')

class PartActionView(FormView_3d_libary):
    model = Part
    form_class = PartForm
    title_prefix = "Teilprojekt"
    success_url = reverse_lazy('3d_libary:parts')

class VariantActionView(FormView_3d_libary):
    model = Variant
    form_class = VariantForm
    title_prefix = "Bauteil"
    success_url = reverse_lazy('3d_libary:variants')
