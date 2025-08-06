from django.views import View
from django.shortcuts import render, redirect
from .TemplateView import AccessData, WebPageAttributeContext

class StandardFormView(View, WebPageAttributeContext, AccessData):
    model = None
    form_class = None
    title_prefix = 'Eintrag'
    success_url = ''
    template_name = 'standard_form_layout.html'

    def get_form_attr(self, title, form, path):
        return {
            'Website': self.get_webpage_attr(),
            'form': {
                'innerBody': form,
                'action': path,
                'title': title
            }
        }

    def get_response(self, request, form, pk):
        title = f"{self.title_prefix} bearbeiten" if pk else f"Neuen {self.title_prefix} speichern"
        return render(request, self.template_name, self.get_form_attr(title, form, request.path))

    def get(self, request, pk=None):
        return self.get_response(request, self.form_class(instance=self.get_instance(self.model, pk)), pk)

    def post(self, request, pk=None):
        instance = self.get_instance(self.model, pk)
        method = request.POST.get('_method', '').upper()

        if method == 'DELETE':
            if instance:
                instance.delete()
            return redirect(self.success_url)

        form = self.form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return self.get_response(request, form, pk)