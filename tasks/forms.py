from django.forms import ModelForm
from tasks.models import Task


class FormularioTask(ModelForm):
    class Meta:
        model = Task
        exclude = ["user"]