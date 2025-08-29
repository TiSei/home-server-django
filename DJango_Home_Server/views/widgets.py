from django import forms
from django.forms.widgets import ClearableFileInput

class CustomFileInput(ClearableFileInput):
    clear_checkbox_label = 'Entfernen'
    initial_text = 'Aktuell'
    template_name = 'widgets/custom_file_input.html'

class ShowImageInput(ClearableFileInput):
    clear_checkbox_label = 'Entfernen'
    template_name = 'widgets/show_image_input.html'