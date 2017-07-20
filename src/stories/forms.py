from django import forms
from django.contrib.auth.models import User

from .models import Story, Branch


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'genre']


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['content']
