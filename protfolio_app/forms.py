from django import forms
from protfolio_app.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fileds =['title', 'description']
