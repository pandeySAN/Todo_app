from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }