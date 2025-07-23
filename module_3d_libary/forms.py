from django import forms
from .models import Tag, Tag_Group

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'desc', 'tag_group']
        labels = {'name':'Name', 'desc':'Beschreibung','tag_group':'Gruppe'}

class TagGroupForm(forms.ModelForm):
    class Meta:
        model = Tag_Group
        fields = ['name', 'color']
        labels = {'name':'Name', 'color':'Farbe'}
