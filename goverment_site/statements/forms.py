from django import forms
from .models import Statement

class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }