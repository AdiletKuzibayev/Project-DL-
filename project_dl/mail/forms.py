from django import forms
from django.forms import ModelForm

from .models import Homework


class UploadFileForm(ModelForm):
    class Meta:
        model = Homework
        fields = ['work_title', 'work_file']