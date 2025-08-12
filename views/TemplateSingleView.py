from views.TemplateView import StandardTemplateView
from django.core.paginator import Paginator

class StandardTemplateSingleView(StandardTemplateView):
    template_name='standard_single_layout.html'
    @staticmethod
    def build_config(title, name, instance, action_url=None, paragraphs=[], details=[]):
        attrs = {'title':title, 'name':name, 'object':instance, 'paragraphs':paragraphs, 'details':details}
        if (action_url):
            attrs['action_url'] = action_url
        return attrs
    @staticmethod
    def build_paragraph(label, content, detail_url=None, classes=[], instance=None):
        attrs = {'label':label, 'content':content, 'classes':classes, 'object':instance}
        if (detail_url and instance):
            attrs['detail_url'] = detail_url
        return attrs
    @staticmethod
    def build_details(summary, new_url, objects, object_template, default_open=True, two_cols=True):
        attrs = {'summary':summary,
                 'new_url':new_url,
                 'objects':objects,
                 'object_template':object_template}
        if (default_open):
            attrs['default_open'] = True
        if (two_cols):
            attrs['two_cols'] = True
        return attrs
    def get_config(pk):
        return {}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Single'] = self.get_config(self.kwargs.get('pk'))
        return context