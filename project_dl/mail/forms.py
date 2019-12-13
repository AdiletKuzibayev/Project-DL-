from django import forms

class UploadFileForm(forms.Form):
    work_title = forms.CharField(max_length=50)
    work_file = forms.FileField()