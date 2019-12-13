from django.forms import ModelForm
from .models import Comment

class CommandForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']