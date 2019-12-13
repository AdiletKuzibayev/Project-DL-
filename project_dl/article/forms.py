
from django.forms import ModelForm
from .models import Commands

class CommandForm(ModelForm):
    class Meta:
        model = Commands
        fields = ['comment_text']
