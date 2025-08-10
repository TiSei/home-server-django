from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

class WebPageAttributeContext:
    def get_webpage_attr(self):
        return {
            'Title':'Home Server',
            'Favicon':'Home_Server_Icon.png',
            'Icon':'Home_Server.png',
        }

class AccessData:
    def get_instance(self, model, pk):
        return None if not pk else get_object_or_404(model, pk=pk)
    def get_all(self, model):
        return model.objects.all()

class StandardTemplateView(TemplateView, WebPageAttributeContext, AccessData):
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Website'] = self.get_webpage_attr()
        return context
