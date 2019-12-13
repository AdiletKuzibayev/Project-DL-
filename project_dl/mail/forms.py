from django import forms
<<<<<<< HEAD

class UploadFileForm(forms.Form):
    work_title = forms.CharField(max_length=50)
    work_file = forms.FileField()
=======
from django.forms import ModelForm

from .models import Homework


class UploadFileForm(ModelForm):
    class Meta:
        model = Homework
        fields = ['work_title', 'work_file']
>>>>>>> parent of 34c64c1... asd
