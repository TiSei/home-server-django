from django.views.generic import TemplateView

def get_standard_webpage_attr():
    return {
            'Title':'Home Server',
            'Favicon':'Home_Server_Icon.png',
            'Icon':'Home_Server.png',
        }

class WebPageAttributeContext:
    webpage_attr = get_standard_webpage_attr()
    
    def get_webpage_attr(self):
        return self.webpage_attr

class StandardTemplateView(TemplateView, WebPageAttributeContext):
    template_name = ''
    data_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Website'] = self.get_webpage_attr()
        context.update({key: qs for key, qs in self.data_context.items()})
        return context
