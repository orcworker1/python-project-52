from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if field_name in self.errors:
                css_class += ' is-invalid'
            field.widget.attrs['class'] = css_class
    first_name = forms.CharField(
        label='Имя',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Пароль должен содержать не менее 3 символов.',
        error_messages={ 'required': 'Введите пароль.',
            'min_length': 'Пароль слишком короткий — минимум 8 символов.',}
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Введите тот же пароль ещё раз для проверки."
    )
    username = forms.CharField(
        label='Имя пользователя',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
        help_text = "150 символов или меньше. Только буквы, цифры и @/./+/-/_."
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','password1','password2')
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

