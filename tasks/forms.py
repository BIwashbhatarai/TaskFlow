from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "is_completed",
            "due_date",
            "priority_choices",
            "category_choices",
        ]
        widgets = {"due_date": forms.DateInput(attrs={"type": "date"})}
