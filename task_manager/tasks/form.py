from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Task
        fields = ['name','description','status','executor','labels']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Описание',
            })
        }