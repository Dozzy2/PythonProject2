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