from django.apps import apps
from views.TemplateView import StandardTemplateView

class IndexTemplateView(StandardTemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['APIs'] = [
            {
                'Name': config.verbose_name,
                'Link': config.link,
                'IconPath': config.icon,
            }
            for config in apps.get_app_configs()
            if config.name.startswith('module_')
        ]
        return context