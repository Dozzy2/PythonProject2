from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}), # Делаем поле datepicker
        }

# class RegisterForm(UserCreationForm): # Пользовательская форма регистрации
#     email = forms.EmailField(required=True)
#
#     class Meta(UserCreationForm.Meta):
#         model = UserCreationForm.Meta.model
#         fields = UserCreationForm.Meta.fields + ('email',) # Добавляем поле email

from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(attrs={'widget_type': 'text'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'widget_type': 'password'}),
        label='Пароль'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'widget_type': 'password'}),
        label='Подтверждение пароля'
    )