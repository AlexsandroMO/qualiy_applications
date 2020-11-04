from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('inspection_name', 'description','link_path_pdf', 'link_path_xlsx')

        