from django import forms
from django.core.exceptions import ValidationError
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 3:
            raise ValidationError("Название задачи должно содержать минимум 3 символа.")
        return title
