
# forms.py
from django import forms
from .models import Project, Segment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'time_to_finish']

class SegmentForm(forms.ModelForm):
    class Meta:
        model = Segment
        fields = ['name', 'description', 'time_to_finish']
