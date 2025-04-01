from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Task
        fields = ["description", "deadline", "tags"]