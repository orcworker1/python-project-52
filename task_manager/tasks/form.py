from django import forms

from .models import Task
from django.contrib.auth import get_user_model
User = get_user_model()

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].queryset = User.objects.all()
        def user_option_label(user: User) -> str:
            full_name = (user.get_full_name() or '').strip()
            return full_name if full_name else user.username
        self.fields['executor'].label_from_instance = user_option_label
    class Meta:
        model = Task
        fields = ['name','description','status','executor','labels']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
            'labels': 'Метки',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
                'rows': 5,
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'executor': forms.Select(attrs={
                'class': 'form-select',
            }),
            'labels': forms.SelectMultiple(attrs={
                'class': 'form-select',
            }),
        }