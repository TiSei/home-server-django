from django import forms
from .models import Part, Project, Tag, Tag_Group, Print_Profil

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

class PrintProfilForm(forms.ModelForm):
    class Meta:
        model = Print_Profil
        fields = ['name', 'desc']
        labels = {'name':'Name', 'desc':'Beschreibung'}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'target']
        labels = {'name':'Name', 'target':'Ziel'}

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'desc', 'project', 'tags']
        labels = {'name':'Name', 'desc':'Beschreibung', 'project':'Projekt', 'tags':'Tags'}
