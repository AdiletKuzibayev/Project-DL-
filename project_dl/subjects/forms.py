from django import forms
from django.forms import ModelForm

from .models import Comment, Student


class CommandForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['teacher_mark']