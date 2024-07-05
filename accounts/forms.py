# from django import forms
# from .models import Project, Module

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'description', 'contributors']

# class ModuleForm(forms.ModelForm):
#     class Meta:
#         model = Module
#         fields = ['project', 'name', 'description', 'estimated_time']

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
