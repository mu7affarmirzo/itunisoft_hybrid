from core.models.services import ProjectFormModel
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectFormModel
        fields = ['full_name', 'phone_number', 'email', 'message']
